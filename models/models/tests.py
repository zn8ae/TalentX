# from django.test import TestCase, Client
# from django.core.urlresolvers import reverse
# from users.models import User
# import json
# #docs.djangoproject.com / testing /tool
# class UserLookupTest(TestCase):
#     fixtures = ['db.json']
#         #setUp method is called before each test in this class
#     def setUp(self):
#         #User.objects.create(uname = 'steven')
#         pass
     

#     def test_lookup_user(self):
#         #response = self.client.get(reverse('look up a user via GET', kwargs={'pk':'1'}))
#         response = self.client.get('/users/Zihan/')
#         #self.assertContains(response,'username')
#         self.assertContains(response,'firstname')
#         user = response.json()
#         self.assertEquals(user['firstname'],'Zihan')
#         self.assertEquals(user['lastname'],'Ni')


#     def test_delete_user(self):
#         response = self.client.post('/users/delete/',{'username':'hq5rc'})

#         #response = self.client.post('/users/delete/',{'id':'hq5rc'})
     
#         # res = response.content.decode('utf-8')
#         # res = json.loads(res)
#         res = response.json()
#         output = {'result':"Success"}
#         # a = response.status_code
#         # self.assertEquals(a,200)
#         self.assertEquals(output,res)
 

#     def test_edit_user(self):

#         response = self.client.post('/users/edit/',{'username':'Zihan','company':'Baidu'})

#         user = response.json()

#         output = {'result':"Success"}
#         self.assertEquals(user['company'],'Baidu')


#     def test_create_user(self):
#        # response = self.client.post('users/create/',{'id':10})
#         response = self.client.post('/users/create/',{'username':'Erzi',
#             'first_name':'DaTou','last_name':'Erzi','email':'dtez@virginia.edu'})
        
#         user = response.json()

#         output = {'status':'success','user_id': 'Erzi'}
#         self.assertEquals(output,user)

     

#     def test_lookup_mission(self):
#         response = self.client.get('/missions/1/')
#         self.assertContains(response,'mname')
#         self.assertContains(response,'desc')
#         user = response.json()
#         self.assertEquals(user['mname'],'Machine Learning Problem')
#         self.assertEquals(user['desc'],'We need a machine learning expert who can help us build a new system!')


     

#     def test_delete_mission(self):

#         response = self.client.post('/missions/delete/',{'id':'2'})
     
#         # res = response.content.decode('utf-8')
#         # res = json.loads(res)
#         res = response.json()
#         output = {'result':"Success"}
#         # a = response.status_code
#         # self.assertEquals(a,200)
#         self.assertEquals(output,res)


#     def test_edit_misson(self):

#         response = self.client.post('/missions/edit/',{'id':'1','mname':'newname'})

#         user = response.json()

#         output = {'result':"Success"}
#         self.assertEquals(user['mname'],'newname')



#     def test_create_misson(self):
#         response = self.client.post('/missions/create/',{'mname':'MissionX',
#             'desc':'DaTou','price':'3000'})
        
#         user = response.json()

#         output = {'status':'success','mission_id': 3}
#         self.assertEquals(output,user)


#     def tearDown(self):
#         pass #nothing to tear down



