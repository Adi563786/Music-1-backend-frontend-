from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from artist.models import Artist
from .models import Follows


class ToggleFollow(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        artist_stage_name = request.GET.get('q')
        print(user,artist_stage_name,"yaha pr ")
        try:
            artist = Artist.objects.get(stage_name=artist_stage_name)
        except Artist.DoesNotExist:
            return Response({"error": "Artist not found"}, status=404)
        print(artist)
        obj, created = Follows.objects.get_or_create(
            user=user,
            artist=artist
        )

        if not created:
            # 🔻 Unfollow
            obj.delete()

            artist.total_followers -= 1
            artist.save()

            return Response({
                "status": "unfollowed",
                "message": f"{artist_stage_name} unfollowed successfully"
            })

        # 🔺 Follow
        artist.total_followers += 1
        artist.save()

        return Response({
            "status": "followed",
            "message": f"{artist_stage_name} followed successfully"
        })