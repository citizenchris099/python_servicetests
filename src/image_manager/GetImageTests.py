"""
tests the image_repo Get image function
"""
import logging
import json
module_logger = logging.getLogger('testlogger')

from ImageManagerTests import imageManagerTests

class getImageTests(imageManagerTests):

    
    # tests getting image blob
#     def test_getImageBlob001(self):
#         module_logger.info('Start test_getImageBlob001')
#                     
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#         
#         # creates new image      
#         imgID, _ = self.createImage01(project_id, user_id, token)
#         
#         # gets image blob
#         response = self.serviceGet02(project_id, user_id, token, self.blobUrl, imgID)
#         
#         self.assertEquals(response.status_code, 200)
#         module_logger.info('PASS: Image Blob was retrieved')
#         
#     # tests Adm creates image 
#     # Adv attempts to get above blob of image
#     # image is in project that Adv should not have access to
#     def test_getImageBlob002(self):
#         module_logger.info('Start test_getImageBlob002')
#                     
#         # gets auth info for Adm
#         project_id1, user_id1, token1 = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#         
#         # gets auth info for Adv
#         project_id2, user_id2, token2 = self.get_token_data(uName = self.enfAdvU, 
#                                                           pWord = self.enfAdvP,
#                                                          listInt = 0)
#         
#         projUuid = "4df0ba7c349340178184a07abbabcc30" 
#         
#         # creates new image      
#         imgID, _ = self.createImage04(project_id1, user_id1, token1, projUuid, 1)
#         
#         # gets image blob
#         response = self.serviceGet02(project_id2, user_id2, token2, self.blobUrl, imgID)
#         
#         
#         self.responseCheck04(response, 401, "Unauthorized", 'PASS: Image Blob was not retrieved')
#         
#         
#     # tests Adv creates image 
#     # Adm attempts to get above blob
#     def test_getImageBlob003(self):
#         module_logger.info('Start test_getImageBlob003')
#                      
#         # gets auth info for Adm
#         project_id1, user_id1, token1 = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#          
#         # gets auth info for Adv
#         project_id2, user_id2, token2 = self.get_token_data(uName = self.enfAdvU, 
#                                                           pWord = self.enfAdvP,
#                                                          listInt = 0)
#          
#         # creates new image      
#         imgID, _ = self.createImage04(project_id2, user_id2, token2, project_id2, 5)
#          
#         # gets image blob
#         response = self.serviceGet02(project_id1, user_id1, token1, self.blobUrl, imgID)
#          
#         self.assertEquals(response.status_code, 200)
#         module_logger.info('PASS: Image Blob was retrieved')
#         
#     # tests Adm creates image 
#     # Adv attempts to get above blob of image
#     # image is in project that Adv should have access to
#     def test_getImageBlob004(self):
#         module_logger.info('Start test_getImageBlob004')
#                     
#         # gets auth info for Adm
#         project_id1, user_id1, token1 = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#         
#         
#         # gets auth info for Adv
#         project_id2, user_id2, token2 = self.get_token_data(uName = self.enfAdvU, 
#                                                           pWord = self.enfAdvP,
#                                                          listInt = 0)
#         self.assertEquals(project_id1, project_id2)
#         
#         # Adm creates new image      
#         imgID, _ = self.createImage04(project_id1, user_id1, token1, project_id1, 5)
#         
#         # gets image blob
#         response = self.serviceGet02(project_id2, user_id2, token2, self.blobUrl, imgID)
#         
#         self.assertEquals(response.status_code, 200)
#         module_logger.info('PASS: Image Blob was retrieved')
#         
#     # tests Adm creates image 
#     # Adv attempts to get above blob of image
#     # image is in project that Adv should have access to
#     # uses normal get w/o ?include_deleted=true"
#     def test_getImageBlob005(self):
#         module_logger.info('Start test_getImageBlob004')
#                     
#         # gets auth info for Adm
#         project_id1, user_id1, token1 = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#         
#         
#         # gets auth info for Adv
#         project_id2, user_id2, token2 = self.get_token_data(uName = self.enfAdvU, 
#                                                           pWord = self.enfAdvP,
#                                                          listInt = 0)
#         self.assertEquals(project_id1, project_id2)
#         
#         # Adm creates new image      
#         imgID, _ = self.createImage04(project_id1, user_id1, token1, project_id1, 5)
#         
#         # gets image blob
#         response = self.serviceGet01(project_id2, user_id2, token2, self.blobUrl, imgID)
#         
#         self.assertEquals(response.status_code, 200)
#         module_logger.info('PASS: Image Blob was retrieved')
#         
#          
#     def test_getImageBlobBadToken(self):
#         module_logger.info('Start test_getImageBlobBadToken')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         imgID, _ = self.createImage01(project_id, user_id, token)
#           
#         # gets image blob
#         response = self.serviceGet02(project_id, user_id, "xxx", self.blobUrl, imgID)
#           
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: Image Blob was not retrieved')
#           
#     def test_getImageBlobBadProjId(self):
#         module_logger.info('Start test_getImageBlobBadProjId')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         imgID, _ = self.createImage01(project_id, user_id, token)
#           
#         # gets image blob
#         response = self.serviceGet02("xxx", user_id, token, self.blobUrl, imgID)
#           
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: Image Blob was not retrieved')
#           
#     def test_getImageBlobBadUsId(self):
#         module_logger.info('Start test_getImageBlobBadUsId')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         imgID, _ = self.createImage01(project_id, user_id, token)
#           
#         # gets image blob
#         response = self.serviceGet02(project_id, "xxx", token, self.blobUrl, imgID)
#           
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: Image Blob was not retrieved')
#           
#     def test_getImageBlobNotFound(self):
#         module_logger.info('Start test_getImageBlobNotFound')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         self.createImage01(project_id, user_id, token)
#           
#         # gets image blob
#         response = self.serviceGet02(project_id, user_id, token, self.blobUrl, 1138)
#           
#         self.assertEquals(response.status_code, 404)
#         module_logger.info('PASS: Image Blob was not retrieved')
#           
#     # tests getting images by user uuid
#     def test_getImageUsr001(self):
#         module_logger.info('Start test_getImageUsr001')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         imgID1, imgID2, _ = self.createImage03(project_id, user_id, token)
#           
#         # gets image based on user uuid
#         response = self.serviceGet02(project_id, user_id, token, self.getUsrUrl, user_id)
#           
#         self.assertEquals(response.status_code, 200)
#         response_data = response.json()
#         message = response_data["content"][0]["id"]
#         message2 = response_data["content"][1]["id"]
#         self.assertEquals(message, imgID1)
#         self.assertEquals(message2, imgID2)
#         module_logger.debug(response_data)
#           
#         module_logger.info('PASS: Images was retrieved')
#           
#     # tests getting images by user id
#     def test_getImageUsr002(self):
#         module_logger.info('Start test_getImageUsr002')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         imgID1, imgID2, _ = self.createImage03(project_id, user_id, token)
#           
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, token, self.getUsrUrl, 1)
#           
#         self.assertEquals(response.status_code, 200)
#         response_data = response.json()
#         message = response_data["content"][0]["id"]
#         message2 = response_data["content"][1]["id"]
#         self.assertEquals(message, imgID1)
#         self.assertEquals(message2, imgID2)
#         module_logger.debug(response_data)
#           
#         module_logger.info('PASS: Images was retrieved')
#           
#     # tests getting images by user id
#     def test_getImageBadUsr001(self):
#         module_logger.info('Start test_getImageBadUsr001')
#           
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, token, self.getUsrUrl, 1138)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#           
#     # tests getting images by user id that has no images
#     def test_getImageBadUsr002(self):
#         module_logger.info('Start test_getImageBadUsr002')
#           
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, token, self.getUsrUrl, user_id)
#         self.assertEquals(response.status_code, 404)
#         module_logger.info('PASS: No Images retrieved')
#           
#     # tests getting images by user bad token
#     def test_getImageUsrBadToken(self):
#         module_logger.info('Start test_getImageUsrBadToken')
#           
#         # gets auth info
#         project_id, user_id, _ = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, "xxx", self.getUsrUrl, user_id)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#           
#     # tests getting images by user bad user id
#     def test_getImageUsrBadUsrID(self):
#         module_logger.info('Start test_getImageBadUsr002')
#           
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # gets images based on user id
#         response = self.serviceGet02(project_id, "xxx", token, self.getUsrUrl, user_id)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#           
#     # tests getting images by user bad user id
#     def test_getImageUsrBadProID(self):
#         module_logger.info('Start test_getImageUsrBadProID')
#           
#         # gets auth info
#         _, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # gets images based on user id
#         response = self.serviceGet02("xxx", user_id, token, self.getUsrUrl, user_id)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#           
#     # tests getting images by project uuid
#     def test_getImageProj001(self):
#         module_logger.info('Start test_getImageProj001')
#                       
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#           
#         # creates new image      
#         imgID1, imgID2, _ = self.createImage03(project_id, user_id, token)
#           
#         # gets image based on user uuid
#         response = self.serviceGet02(project_id, user_id, token, self.getProUrl, project_id)
#           
#         self.assertEquals(response.status_code, 200)
#         response_data = response.json()
#         message = response_data["content"][0]["id"]
#         message2 = response_data["content"][1]["id"]
#         self.assertEquals(message, imgID1)
#         self.assertEquals(message2, imgID2)
#         module_logger.debug(response_data)
#           
#         module_logger.info('PASS: Images was retrieved')
#           
#     # tests getting images by project id
#     def test_getImageProj002(self):
#         module_logger.info('Start test_getImageProj002')
#                        
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#            
#         # creates new image      
#         imgID1, imgID2, _ = self.createImage03(project_id, user_id, token)
#            
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, token, self.getProUrl, 5)
#            
#         self.assertEquals(response.status_code, 200)
#         response_data = response.json()
#         message = response_data["content"][0]["id"]
#         message2 = response_data["content"][1]["id"]
#         self.assertEquals(message, imgID1)
#         self.assertEquals(message2, imgID2)
#         module_logger.debug(response_data)
#            
#         module_logger.info('PASS: Images was retrieved')
# #         
#     # tests getting images by bad project id
#     def test_getImageBadProj001(self):
#         module_logger.info('Start test_getImageBadProj001')
#            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#            
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, token, self.getProUrl, 1138)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#            
#     # tests getting images by project id that has no images
#     def test_getImageBadProj002(self):
#         module_logger.info('Start test_getImageBadProj002')
#            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#            
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, token, self.getProUrl, project_id)
#         self.assertEquals(response.status_code, 404)
#         module_logger.info('PASS: No Images retrieved')
#            
#     # tests getting images by user bad token
#     def test_getImageProjBadToken(self):
#         module_logger.info('Start test_getImageProjBadToken')
#            
#         # gets auth info
#         project_id, user_id, _ = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#            
#         # gets images based on user id
#         response = self.serviceGet02(project_id, user_id, "xxx", self.getProUrl, user_id)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#            
#     # tests getting images by user bad user id
#     def test_getImageProjBadUsrID(self):
#         module_logger.info('Start test_getImageProjBadUsrID')
#            
#         # gets auth info
#         project_id, _, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#            
#         # gets images based on user id
#         response = self.serviceGet02(project_id, "xxx", token, self.getUsrUrl, project_id)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
#            
#     # tests getting images by user bad user id
#     def test_getImageProjBadProID(self):
#         module_logger.info('Start test_getImageProjBadProID')
#            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#            
#         # gets images based on user id
#         response = self.serviceGet02("xxx", user_id, token, self.getUsrUrl, project_id)
#         self.assertEquals(response.status_code, 401)
#         module_logger.info('PASS: No Images retrieved')
        
    def test_getImageName001(self):
        module_logger.info('Start test_getImageName001')
        
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": "Veggie",
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"tiff",
                         },{"url": self.testUrl,
                           "name": "Pappa",
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"jpeg",
                         }
                                        ]})
        # posts data and returns response
        response = self.postImage(project_id, user_id, token, serviceUrl=self.serviceUrl, 
            data=imgData)
        
        # checks response
        imgID1 = self.responseCheck02(response, key="url", 
            expected=self.testUrl, 
            listInt=0, 
            code=201, 
            logMsg='new image 1 created')
        
        imgID2 = self.responseCheck02(response, key="url", 
            expected=self.testUrl, 
            listInt=1, 
            code=201, 
            logMsg=' new image 2 created')
        self.added_imageIds.append(imgID1)
        self.added_imageIds.append(imgID2)
        
        _, name1 = self.postResponseMessage(response, 0, "name")
        _, name2 = self.postResponseMessage(response, 1, "name")
        
        
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, self.getNamUrl, 
                                          image_id = name1)
        response_data = response2.json()
        message = response_data["content"][0]["name"] 
        self.assertEquals(message, name1)
        
        response3 = self.serviceGet01(project_id, user_id, 
                                          token, self.getNamUrl, 
                                          image_id = name2)
        response_data = response3.json()
        message = response_data["content"][0]["name"] 
        self.assertEquals(message, name2)
        
                
        module_logger.info('PASS: Images were retrieved by Name')
         
 
         
 
     



            