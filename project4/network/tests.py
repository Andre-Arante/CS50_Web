# from django.test import Client, TestCase
# from django.db.models import Max

# from .models import Post, User, UserProfile, Friendship

# # Create your tests here.
# class NetworkTestCase(TestCase):

#     def setUp(self):

#         # Create test users
#         self.mooshy = User.objects.create(username='mooshy', password='password')
#         self.andre = User.objects.create(username='andre', password='password')
#         self.mooshy_profile = UserProfile.objects.create(user=self.mooshy)


#         # Create a post
#         Post.objects.create(content='test post 1', user=self.mooshy)
#         Post.objects.create(content='test post 2', user=self.mooshy)
#         Post.objects.create(content='test post 3', user=self.andre)

#         # Create a friendship link (mooshy -> andre)
#         f1 = Friendship(root=self.mooshy, following=self.andre)

#     def test_user_posts(self):
#         """ Makes sure Mooshy has the correct number of posts """
#         mooshy_posts = Post.objects.filter(user=User.objects.get(username='mooshy'))
#         self.assertEqual(mooshy_posts.count(), 2)
    
#     def test_user_followers(self):
#         """ Makes sure andre has 1 follower """
#         c = Client()
#         response = c.get('/index/')

#         self.assertEqual(response.content)
        

#         # m = User.objects.get(username='mooshy')
#         # response = c.get(f'/profile/${m.username}')


    

