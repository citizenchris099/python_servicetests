"""
tests the image_repo Update/Patch image function
"""
import logging
import json
module_logger = logging.getLogger('testlogger')

from ImageManagerTests import imageManagerTests

class updateImageTests(imageManagerTests):

    
    #tests patching/updating an image
    # passes only the 5 required attributes in payload
    def test_updateImage001(self):
        module_logger.info('Start test_updateImage001')
                    
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # creates new image      
        imgID, _ = self.createImage01(project_id, user_id, token)
        
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "name": "Veggie",
                                "width":500,
                                "height":500,
                                "type":"tiff",
                                "thumb":True,
                                "portrait":True,
                                "used":True,
                                "hold_expire":1417631818,
                                "current":True,
                                "deleted":True
                                })
        
        # updates the above created image
        response = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
        
        # checks response of patch
        self.responseCheck02(response, "url", "kittens/eating.jpg", 0, 200, 'new image patched')
        
        
        # gets patched image
        response2 = self.serviceGet02(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        
        # insures patched data intact  
        _, message = self.getResponseMessage(response2, key = "name")
        self.assertEquals(message, "Veggie")
        _, message = self.getResponseMessage(response2, key = "width")
        self.assertEquals(message, 500)
        _, message = self.getResponseMessage(response2, key = "height")
        self.assertEquals(message, 500)
        _, message = self.getResponseMessage(response2, key = "type")
        self.assertEquals(message, "tiff")
        _, message = self.getResponseMessage(response2, key = "thumb")
        self.assertEquals(message, 1)
        _, message = self.getResponseMessage(response2, key = "portrait")
        self.assertEquals(message, 1)
        _, message = self.getResponseMessage(response2, key = "used")
        self.assertEquals(message, 1)
        _, message = self.getResponseMessage(response2, key = "hold_expire")
        self.assertEquals(message, 1417631818)
        _, message = self.getResponseMessage(response2, key = "current")
        self.assertEquals(message, 1)
        _, message = self.getResponseMessage(response2, key = "deleted")
        self.assertEquals(message, 1)
     
    # posts image then tries to patch w/o valid token    
    def test_updateImageBadToken(self):
        module_logger.info('Start test_updateImageBadToken')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
          
        # creates new image        
        imgID, _ = self.createImage01(project_id, user_id, token)
          
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "name": "Veggie",
                                "width":500,
                                "height":500,
                                "type":"tiff"
                                })
          
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          "xxx", serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
          
        # checks response
        self.responseCheck01(response2, code = 401, 
                             expected = "Unauthorized", 
                             passMsg = 'PASS : status code was 401, new_id was None and message was "not authorized"', 
                             failMsg = 'FAIL : status code was not 401')
          
    # posts image then tries to patch w/o valid proj_id    
    def test_updateImageBadProjId(self):
        module_logger.info('Start test_updateImageBadProjId')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
          
        # creates new image        
        imgID, _ = self.createImage01(project_id, user_id, token)
          
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "name": "Veggie",
                                "width":500,
                                "height":500,
                                "type":"tiff"
                                })
          
        # updates the above created image
        response2 = self.patchImage("xxx", user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
          
        # checks response
        self.responseCheck01(response2, code = 401, 
                             expected = "Unauthorized", 
                             passMsg = 'PASS : status code was 401, new_id was None and message was "not authorized"', 
                             failMsg = 'FAIL : status code was not 401')
          
    # posts image then tries to patch w/o valid user_id    
    def test_updateImageBadUsrId(self):
        module_logger.info('Start test_updateImageBadUsrId')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
          
        # creates new image        
        imgID, _ = self.createImage01(project_id, user_id, token)
          
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "name": "Veggie",
                                "width":500,
                                "height":500,
                                "type":"tiff"
                                })
          
        # updates the above created image
        response2 = self.patchImage(project_id, "xxx", 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
          
        # checks response
        self.responseCheck01(response2, code = 401, 
                             expected = "Unauthorized", 
                             passMsg = 'PASS : status code was 401, new_id was None and message was "not authorized"', 
                             failMsg = 'FAIL : status code was not 401')
          
    # posts image then tries to patch w/a bad url  
    def test_updateImageBadUrl(self):
        module_logger.info('Start test_updateImageBadUrl')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
          
        # creates new image        
        imgID, _ = self.createImage01(project_id, user_id, token)
          
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "name": "Veggie",
                                "width":500,
                                "height":500,
                                "type":"tiff"
                                })
          
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.serviceUrl, 
                          data = patchData, 
                          image_id = imgID)
          
        # checks response
        self.responseCheck01(response2, code = 404, 
                             expected = "Not Found", 
                             passMsg = 'PASS : status code was 404, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 404')
          
    # posts image then tries to patch user id
    def test_updateImageBadData001(self):
        module_logger.info('Start test_updateImageBadData001')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "user_id": "b9be2369ff09432ba322e8e840b48a90"
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch project id
    def test_updateImageBadData002(self):
        module_logger.info('Start test_updateImageBadData002')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "project_id": "4df0ba7c349340178184a07abbabcc30"
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch resolution
    def test_updateImageBadData003(self):
        module_logger.info('Start test_updateImageBadData003')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "resolution": 1080
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch uuid
    def test_updateImageBadData004(self):
        module_logger.info('Start test_updateImageBadData004')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "uuid": "befe0806-7b19-11e4-b116-123b93f75cba"
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch date
    def test_updateImageBadData005(self):
        module_logger.info('Start test_updateImageBadData005')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "date":1417631818
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch last_update
    def test_updateImageBadData006(self):
        module_logger.info('Start test_updateImageBadData006')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "last_update":1417631818
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch parent
    def test_updateImageBadData007(self):
        module_logger.info('Start test_updateImageBadData007')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "parent":1007
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
         
    # posts image then tries to patch ancestor
    def test_updateImageBadData008(self):
        module_logger.info('Start test_updateImageBadData008')
                       
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
           
        # creates new image        
        imgID, response = self.createImage01(project_id, user_id, token)
           
        patchData = json.dumps({"url": "kittens/eating.jpg",
                                "ancestor":1007
                                })
           
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
           
        # checks response
        self.responseCheck01(response2, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'status code of patch was 400, new_id was None and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')
          
        _, message = self.getResponseMessage(response, key = "url")
        self.assertEquals(message, self.testUrl)
        module_logger.info('PASS : image data was not patched')
