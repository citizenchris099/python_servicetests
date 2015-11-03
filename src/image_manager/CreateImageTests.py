"""
tests the image_repo Create /Post image function
"""
import logging
import json
module_logger = logging.getLogger('testlogger')

from ImageManagerTests import imageManagerTests

class createImageTests(imageManagerTests):

    
    #tests posting a image 
    # passes only the 5 required attributes in payload
    def test_createImage001(self):
        module_logger.info('Start test_createImage001')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"url", self.testUrl,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image retrieved from db')
         
         
    #tests posting a student using the student manager
    # passes the 5 required attributes in payload as well as user_id
    def test_createImage002(self):
        module_logger.info('Start test_createImage002')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "user_id":"b9be2369ff09432ba322e8e840b48a90"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"user_id", 2,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 2, "user_id", passMsg='new image retrieved from db')
        
          
    #tests posting a student using the student manager
    # passes the 5 required attributes in payload as well as project_id
    def test_createImage003(self):
        module_logger.info('Start test_createImage003')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "project_id":"4df0ba7c349340178184a07abbabcc30",
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"project_id", 1,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 1, "project_id", passMsg='PASS: Image was retrieved from db')
          
    #tests posting a student using the student manager
    # passes the 5 required attributes in payload as well as project/user_id
    def test_createImage004(self):
        module_logger.info('Start test_createImage004')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "project_id":"4df0ba7c349340178184a07abbabcc30",
                           "user_id":"b9be2369ff09432ba322e8e840b48a90"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"project_id", 1,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 1, "project_id", passMsg='PASS: Image was retrieved from db')
          
    #tests posting a student using the student manager
    # passes the 5 required attributes in payload as well as project/user_id
    # using adviser level enfold credentials. does not use include deleted true
    def test_createImage005(self):
        module_logger.info('Start test_createImage005')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdvU, 
                                                          pWord = self.enfAdvP,
                                                         listInt = 0) 
                
        # data to be used in post
        # the user and project are not affiliated with the enfold user
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "project_id":"4df0ba7c349340178184a07abbabcc30",
                           "user_id":"45a9c0c889ab4b80813c4938a5b9d914"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"project_id", 1,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 1, "project_id", passMsg='PASS: Image was retrieved from db')
          
    # passes the 5 required attributes in payload including thumb
    def test_createImage006(self):
        module_logger.info('Start test_createImage006')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "thumb":True
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"thumb", 1,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 1, "thumb", passMsg='PASS: Image was retrieved from db')
          
    # passes the 5 required attributes in payload including portrait
    def test_createImage007(self):
        module_logger.info('Start test_createImage007')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "portrait":True
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"portrait", 1,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 1, "portrait", passMsg='PASS: Image was retrieved from db')
        
          
    # passes the 5 required attributes in payload including resolution
    def test_createImage008(self):
        module_logger.info('Start test_createImage008')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "resolution":8388607
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"resolution", 8388607,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, 8388607, "resolution", passMsg='PASS: Image was retrieved from db')
          
    # passes the 5 required attributes in payload including uuid
    def test_createImage009(self):
        module_logger.info('Start test_createImage009')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "uuid":"befe0806-7b19-11e4-b116-123b93f75cba"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"uuid", "befe08067b1911e4b116123b93f75cba",0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "befe08067b1911e4b116123b93f75cba", "uuid", passMsg='PASS: Image was retrieved from db')
          
    #tests posting a student using the student manager
    # passes the 5 required and optional attributes
    def test_createImage010(self):
        module_logger.info('Start test_createImage010')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "project_id":"4df0ba7c349340178184a07abbabcc30",
                           "user_id":"b9be2369ff09432ba322e8e840b48a90",
                           "uuid":"befe0806-7b19-11e4-b116-123b93f75cba",
                           "resolution":8388607,
                           "portrait":True,
                           "thumb":True
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"project_id", 1,0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "befe08067b1911e4b116123b93f75cba", "uuid", passMsg='PASS: Image was retrieved from db')
          
        _, message = self.getResponseMessage(response2, key = "name")
        self.assertEquals(message, self.testName)
        _, message = self.getResponseMessage(response2, key = "width")
        self.assertEquals(message, self.testWidth)
        _, message = self.getResponseMessage(response2, key = "height")
        self.assertEquals(message, self.testHeight)
        _, message = self.getResponseMessage(response2, key = "type")
        self.assertEquals(message, self.testType)
        _, message = self.getResponseMessage(response2, key = "user_id")
        self.assertEquals(message, 2)
        _, message = self.getResponseMessage(response2, key = "uuid")
        self.assertEquals(message, "befe08067b1911e4b116123b93f75cba")
        _, message = self.getResponseMessage(response2, key = "resolution")
        self.assertEquals(message, 8388607)
        _, message = self.getResponseMessage(response2, key = "portrait")
        self.assertEquals(message, 1)
        _, message = self.getResponseMessage(response2, key = "thumb")
        self.assertEquals(message, 1)
          
    # passes type as 'jpeg'
    def test_createImage011(self):
        module_logger.info('Start test_createImage011')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"jpeg",
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"type", "jpeg",0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "jpeg", "type", passMsg='PASS: Image was retrieved from db')
        
          
    # passes type as 'png'
    def test_createImage012(self):
        module_logger.info('Start test_createImage012')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"png",
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"type", "png",0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "png", "type", passMsg='PASS: Image was retrieved from db')
          
    # passes type as 'tiff'
    def test_createImage013(self):
        module_logger.info('Start test_createImage013')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"tiff",
                         }
                                        ]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"type", "tiff",0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "tiff", "type", passMsg='PASS: Image was retrieved from db')
        
    #tests posting an image as an Adviser
    # passes only the 5 required attributes in payload
    def test_createImage014(self):
        module_logger.info('Start test_createImage014')
                    
        # gets auth info for Adv
        project_id2, user_id2, token2 = self.get_token_data(uName = self.enfAdvU, 
                                                          pWord = self.enfAdvP,
                                                         listInt = 0) 
              
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                
        # posts data and returns response 
        response = self.postImage(project_id2, user_id2, 
                   token2, serviceUrl = self.serviceUrl, 
                   data = imgData )
             
        # checks response
        imgID = self.responseCheck02(response,"url", self.testUrl,0, 201, "image was created")
        
        response2 = self.serviceGet02(project_id2, user_id2, token2, serviceUrl=self.getUrl, image_id = imgID)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image retrieved from db')
    
    # posts two images     
    def test_createImage015(self):
        module_logger.info('Start test_createImage013')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"tiff",
                         },{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"jpeg",
                         }
                                        ]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        imgID = self.responseCheck02(response,"type", "tiff",0, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "tiff", "type", passMsg='PASS: Image was retrieved from db')
        
        imgID = self.responseCheck02(response,"type", "jpeg",1, 201, "image was created")
         
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, "jpeg", "type", passMsg='PASS: Image was retrieved from db')
          
          
    #insures you can't post SM data w/o a token   
    def test_createImageBadToken(self):
        module_logger.info('Start test_createImageBadToken')
                  
        # gets auth info
        project_id, user_id, _ = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
               
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                 
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   "xxx", serviceUrl = self.serviceUrl, 
                   data = imgData )
           
        # checks response
        self.responseCheck01(response, code = 401, 
                             expected = "Unauthorized", 
                             passMsg = 'PASS : status code was 401, new_id was None and message was "not authorized"', 
                             failMsg = 'FAIL : status code was not 401')
              
                    
    # insures you can't get SM info w/o a valid project_id   
    def test_createImageBadProjId(self):
        module_logger.info('Start test_createImageBadProjId')
                   
        # gets auth info
        _, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
               
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                 
        # posts data and returns response 
        response = self.postImage("xxx", user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
           
        # checks response
        self.responseCheck01(response, code = 401, 
                             expected = "Unauthorized", 
                             passMsg = 'PASS : status code was 401, new_id was None and message was "not authorized"', 
                             failMsg = 'FAIL : status code was not 401')
                 
    # insures you can't get SM info w/o a valid user_id   
    def test_createImageBadUsrId(self):
        module_logger.info('Start test_createImageBadUsrId')
                   
        # gets auth info
        project_id, _, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
               
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                 
        # posts data and returns response 
        response = self.postImage(project_id, "xxx", 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
           
        # checks response
        self.responseCheck01(response, code = 401, 
                             expected = "Unauthorized", 
                             passMsg = 'PASS : status code was 401, new_id was None and message was "not authorized"', 
                             failMsg = 'FAIL : status code was not 401')
                 
    # insures you can't get SM info w/o a valid url   
    def test_createImageBadUrl(self):
        module_logger.info('Start test_createImageBadUrl')
                   
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = '{0:s}/api_1_0/images/', 
                   data = imgData )
            
        # checks response
        self.responseCheck01(response, code = 404, 
                             expected = "Not Found", 
                             passMsg = 'PASS : status code was 404, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 404')
           
             
    # attempts to post w/o passing url in the payload
    def test_createImageBadData001(self):
        module_logger.info('Start test_createImageBadData001')
                   
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        # lacks the required url
        imgData = json.dumps({"images":[{"name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
            
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
             
                
    # attempts to post w/o passing name in the payload
    def test_createImageBadData002(self):
        module_logger.info('Start test_createImageBadData002')
                   
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        # lacks the required name
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
            
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # attempts to post w/o passing width in the payload
    def test_createImageBadData003(self):
        module_logger.info('Start test_createImageBadData003')
                   
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        # lacks the required width
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})                
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
            
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # attempts to post w/o passing height in the payload
    def test_createImageBadData004(self):
        module_logger.info('Start test_createImageBadData004')
                   
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        # lacks the required height
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "type":self.testType
                         }]})
                       
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
            
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # attempts to post w/o passing type in the payload
    def test_createImageBadData005(self):
        module_logger.info('Start test_createImageBadData005')
                   
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        # lacks the required type
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                         }]})
                       
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
            
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a bad resolution int
    def test_createImageBadData006(self):
        module_logger.info('Start test_createImageBadData006')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "resolution":8388608
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a bad resolution int
    def test_createImageBadData007(self):
        module_logger.info('Start test_createImageBadData007')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "resolution":-50
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a bad resolution int
    def test_createImageBadData008(self):
        module_logger.info('Start test_createImageBadData008')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "resolution":50.5
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid id attribute
    def test_createImageBadData009(self):
        module_logger.info('Start test_createImageBadData009')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "id":1138
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid date attribute
    def test_createImageBadData010(self):
        module_logger.info('Start test_createImageBadData010')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "date":1417631818
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid used attribute
    def test_createImageBadData011(self):
        module_logger.info('Start test_createImageBadData011')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "used":True
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid hold_expire attribute
    def test_createImageBadData012(self):
        module_logger.info('Start test_createImageBadData012')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "hold_expire":1417631818
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid current attribute
    def test_createImageBadData013(self):
        module_logger.info('Start test_createImageBadData013')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "current":False
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid last_update attribute
    def test_createImageBadData014(self):
        module_logger.info('Start test_createImageBadData014')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "last_update":1417631818
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid parent attribute
    def test_createImageBadData015(self):
        module_logger.info('Start test_createImageBadData015')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "parent":1138
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid ancestor attribute
    def test_createImageBadData016(self):
        module_logger.info('Start test_createImageBadData016')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "ancestor":1138
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes what should be a invalid deleted attribute
    def test_createImageBadData017(self):
        module_logger.info('Start test_createImageBadData017')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType,
                           "deleted":True
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes url that excedes the documented limit
    def test_createImageBadData018(self):
        module_logger.info('Start test_createImageBadData018')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": "6ePCtwYjgqqSA0YJSEcS6WOJwIyFm1IpwgHbwym3MjYvnCzkfIIYlrKbQc9uwvVNEeJS6RI9HPKHS2myvfXhTcv1fQOCKtFqnGeALDbGVJfuWMrqHJ2STorbi5QkKO9vD5UoIDg3oNG2eUNqmVKnnit2YX2aeSbye3xOo28NPwABDtHGl3boIuE9CRg4r6LISxvuPzHiZZnCWeCt1gwioX3kcDlEUM1jxwNZGRg0Y3zbIw9SPl69THROPKcEw9pGVRb18aTVNKTJrypMLHO42nHSsUjTII1inmLDp8W2lSSWVKt2sBwyjoeASQae5Lp0P4vXcWFqq2yTYwgXhD3hB53I0gnO7fmLc1g2DKgcaIwwg4u0Nn98fkO8ncALeL7iUTZThf45DC9gtN2JtqRr87tiLz0QYYPgFefWuz8VGvbZKtuZzB3jjJYVoS2BI48yzKGy3pNE6Umch8OojqiBsT58Xj5zfE9VnVgXYqLmWturgXvZnNSI6jxGiWIUSJCN3RblxMkKb9MUYrSjx18VIohoZo5aL7hiEmCbG8MMA6gthMzsyY6R8i80suxjlVyAfg7UDHfwLovM7IjCrEcam5Kb8mr07owzm3LHFByiBfMHDi0KQLqBrpwO2HshMY1xrLhDaAx4Tsb23a1yIPAaL12prkL8mE4nFVt27Lwaa1bnm1IFhlVHt0JYRTONMtyP55X9vTV3M6qiHfc6aeWu9RC0o1aQIl48Ph8ShEqzm2DNqNrZTzslR4vK3uBQw9hNHRjXmg1clXZZfzvwwCQNhQgHJPx9y52GWK8n3rDTWgAXxE55yXMEb8tnX5EVE7lorAsRBqINaA8Z47nPb0VBfSinjRMqYS2KMu2QYsnsg38YTVYhHJ2iMuuzNx1zZI6K3LWw2jqgewV5s7km6AjyfASGJSaMJY2ww6SeQe2XPllI0i6w8OSSs3S3zOhVnCtKERV1c1mGCgoAjaaiqNK9rglChrAJVY9awHvCzvuZjvmfrJtSRUMElxI9JiEfnR6vlnuo5YNlqkVI2eocnn2cDYnUzSLGPSYocTKPXiiD8uPqDGj3LxoQCoag3xuq8UMScPQ6ZOqcqkwjkClzYkfn6zoIrlEpE3LSHURUtS0UoNbnEVqUsZIpnPIkmupy9BC4VSLDesxwVW3eO8ziT1TEoHJ1EMEEjnQWIyFFZTwnxxQ5YKr24stmiXpwisCpZhq6EfI0YboiwXzVZ25f9es03R0gH5RFf6LXifSaGhhEfqwThT3h0ZlpuGcG95f28HRpLMfg0FrQRkxZW3EPY2pOsqoMD1rFa5GYz4omDnyU7Sx0eAr9JAgujOhOFwwhJcReDBa4wVCnv8bF6s3sv4FqADOpKhQrTDBbBOzuOUMry034gCkCv8Ei16cIHiabpGPkpVXcSsEnyKLo53p7CmNHKIkZsv4N0FDv5ZwJG7M9nCtIjmsliBOIJejp5sAMXxUoPhW6o9lkAJKjpimTJqmxuQnV1p1eNFj0gQmG6F69PhvZFMMqnQ6w2QXKuycljRlBYqAn6sL5oUgPi8tuwk4obb1ElEKgULQDtqvR3Hgh9oF0KtMOhSfLTELUZHJ45lEb3qPlEhExFsf6vktKLFfQ1WjeI1E9eKrxcAYhqWZvw5prOGIWuHBplmXY5zrFyl0UaGlAS7EZWQKG19uh4HV3EntNInUny4yHH1EWMGEEIuvXOpW7csxJlKDljrpIkXtE9XKtM5xQgVjRWLnOJehoZNcfPFF4tWawMlwscMjOYrfX8j7ebry1tMZq4fVk7YiRhr2DbPC1WX4obUYTqILT1J5Am3lE7j5bC03rZKfTIOLSpPC5v4I0PsF1uACBE08b4GICAHRAuCfRgeslZnzQCLGA5RSmUScozur7vL1bponSfeF7i1PmHZ1Y2LOghqsW8K8gUHk9e1fl54uNl2IebJTheC4HocNJS9LVVGWRcUHl5zIOz8KjpPoEvPQ3RpFER8OngymzaQ2SOIzc4mvnCEjr06P4WFOhxrtT05fvT96jWKGg1AJ71BlpBzhnA3yAeVF8MJQiMcsYufosnIEpXOmeCqrgFw77YLyhWllCBVTa8zhHLKAGic2gRBaKAkqiAHgKlsB3JOlfWDYLIlGMeKHARURU1WPVWFM30ybhv4D3bKe25q4VeSrinkupU5t7vEcSoKzlJZZKxQ4oJg8RblsT3m1cM2yncK6tvFztJBotuWzqnF7uZ7Dfy1aLcc3MsykfHv7QhCnKVMpWSqTq8MsqHN6cEUFLpJPApugN4A3K7N0GF078JQ43YTFZsuVOCQZ4brk8ohn4QjS9lCt7HEDRlMKz8BDzKwXKbGrUOkBBHX3XElfofjVm61XxTMybHFoKDaf8ub7JUmYcIDcbyWbVkfsUmfhTRbraGQT4rgoI36sbl1DZNcg16t4EFXpOINPevhgA7jfpoTZnP9ELi3UNxALuI003z4suHwnIs5oa50mBQUNqYHqIAfaVF1c2HPXDKheFLk91ZYjxzVOA8TuHiJBCKaa4BIJeXbJSfLx4uxFlblNwnqgmppZOj2gey46NwDUuxHneDMEGyGrqLPKsZ7wgX7lhsYNkNopRFxX2AFjT5bBTpupKv309ifDePEzJ0UaC5IKXeDqt0ceF2LXWYLZxuruJaZfMYEwF3VkI3AsIJWjA6Bz2AnLKq0A0uwQcfFgEjsKZr2WKxpgPSb7JifKhWQoS3j22qAfyPR0lNDUGwFstW1QhXD9OnXJ5DvVhMA4F6TNpvJL5Oh65V8cttNUxfkQXxNOE4U5CnDvhCpiGV3jStDXVkfIDpUn6pkCNBpyQgTua2EWjvZiNpkwAjit6g4XEQK6FAt9fJWAt2Ln6cv65gUysxOSUhZLnECLYL5NX6iSHJ3h0WTo2T4RFEio6KBsvVUEiahsFwVG68Ompe4pTA3sKn7gwTBomNYBTkHuRpMPibuE7Vyr95pV5a5Zs2KVy6vHmpx5yyf73g35BbAj4gV0MleWObsffyZXZZz4729cJHPhpzKaiA2vx9JcoOD7MWfhRREItKZqqOhuPuAIXm9j2soMmQFatKgAI1e6rRbeOZkZZXAkSFvOti0S5XOfIXmqw6jCpPQx15GDSrqI036u8ZeEi6H3g4rsVVwwgsGFQ5DyW3rPc52KHpyZ7hebStFyfju7ob4b4ZSfH3jMepW1glDKXwu97UhXuexRgSzgf0PRKr2fWRKaXkP00hgSqmCHJ4sRUzu5xRWMWTf2P3F0KEVRsMonr2AiNjJDVyROXztkS1vUGZvcmzc7IZKyzMcKYgR2yTzkLcoRxJaCF66oDMJD3tfwTvpGjcXy3TKF6bA3iVkhsm8uXcTxhK4W949NNJHGq4su0yit6sWTNP1l8WaVQOqF8kRD5kpMfczPsFKgZerbfnkukA7KbU7GfqSpm8pXMKY5U8chEKkK3x4qiALXexQjglnjjcIltrVmWW3mxHfbyRGKY81R6IkwwIsRGGQuv6HN6NkRXW5TvgQYi4yKozZKfUvHMrZeGUAzeSgrAFDIULPc19KPe0KDYjLsiVmwDBWGHEo5aN270yXmcy4hWRZkCNaZvhPNabFng4DrrI1tr1msBAvIR32PjJtPzzNlWNOxOWNimbXBNnZcqHpNmbAIVRxPcwl2hNwxHCbqxxqFlfSYsLw34jzYxD19sfyrp8ca4NCBY2MaXIBKcwe8zTbeiR7wRjbQM0TWBQzU0Emlrw4yvi842bj7tpLwPczTMGVDh0CguWuBWvv3c3O0rGV1SiOreOChxERUMb89ff3xJiIpgFPYHT2TkZR7bioB6WDxKNhOM4eP9kymYi3amoFuw3Scl6vOUQVswT2ojSmHUZIzueeff6eI8NrA2ubwhFSnZDQuNTintcHiAQATGN2p9pZ35TlKpSYxUQ74CnLWRX66EQ6RFSa6phwixUQZuxcHa0lp2XbsHq4b2KE1potmrxk1Ljjn7Qqpzk6lntxfh47utGwJfjVZzQ8xWqR5T24vFbES3IEqcg2pTjiuy6cTevwjxHkgly5R1Mw18JEN4IfIt4KN8qtUxFkXeywL1g0rz0uJ1eGTrM9xMMinLcoV7XIuZpZAZepvkDLcmeSj2o7MsclqUSzoek7Hw8Ocnxx8hGqwh0AbnFgIQcfmRX0TZWESJyKpgmi2y37jRmNcizMO6V9DZLX86IELHgA8UohtVxZROPVu7UuUqfxTju06yEAJMLMS3qiznLQqqCMZOvuswzrphqkqIM7hURp2CeVP2OEGOnI7sGgcsOtBPwh3MbsBh58GzFyRuJ8Cjq9u0YR2DFJZEaffcjUH5GLv36mqYtOwebiYi3r442bnPaFCBsNvQBJ5OWQDh39gLQ46c2VZTP46v6nFPFuhvV1pPAwxtWXPgkqBhOaF6UMP2L6ojLOmfmmt9sGNfH89AoFbgS40FpRjfVn9yEA6f6sl8sFOcUz9VbkEic74F7ixXvwX5Ot6O0JoMvePDilZDO0bXy9pSmZcSEYLvc5AONeKnvcAk7bBxkH0YMmDzPIfuqUbGhp86Jz1mlpXPR7wlRa3HJtmrYTMurYtygcDDqxjxmO4T6uTk8Kci4obYq6eiZqvKJ4skUxmqUVv2GYQj6huSAPaSIuFOkmpPtoWA1z7SftKA2gRRNgE1wlnTmyww3l6voH2RXku0Ci6JZvJKFs6wsyFNXfoK4cfhZokw5x7lGty2tsyERwSk7LVGSbfcu5ncQn4U6GU97P58PwV61ZWNHyjrNgJSUOm6llTNiKfbrscx6gCGauRegSUzQiRT1l2JS0gT9sPr9KEUN3jwPfxvsjAaLfU0jGar3KwOgAIq9surC2BUzIjbvu3ftiu34Xy1ir44hAosg9fwNmkoBIhFqVi8IyWKMCrLAxSynyooaUwInt6OKsTFpZ1n9J4Kt6hJBq32MbXqy6ISTX8UB8KZCaJCwfSWEDvsY0V6Bl2jnH1AiseUXDCyawE2bqP1efOFRD8gVvtGzyJP2J2zxrTufu7IS57hP6yoJ27caOxLSaFUzgJkQU0MCQgsEnpAl8llsOPAF2DeYwZERPCJpKoUm1JM7DEMDKZoAWDJs4fjRefNswlfaIrRMwWh3QebDWLvSEzQrvferZwGtP35fyTlGIiZX7mpwEEMbyJiGufSng394b3yHgqlOQRkesIjoc7JtV0hZTsBh2VKaEvjTzlJufcThIjsTh2W2k0GLGBr1e67cIthPBPpHTuY33CxjQNQftg94v7soOHKnGgrQTaoe6OTSm0eRAKP9hFw1CHsSItK0XU8wDio6ATPiYkb9kPyGgbijXXKUAxbeN3wV1FwpELPnRKt2XzwS3NF3Btr9XuoQfS9Y7li5I35hO1SBu9UtnHwUgWH6KxFvis69MgOl4bsQYMXnjUGHYHPqjJu1O6h5pf3tNNlUV7bKG8VYNWRj60hxMwo1Uyul3WNxtGUVw31FoG0N51aV264uQnNqQa7PPwT6iYtNNGlI4uY5bQODXX6WmUhpRs61vqHJSrXs1qNjIAY9hjzFZulcLMcOlByJvcwDf2TMS4Y32AxYei7xDfhUgoHmFmJLDi4YeU6nCHx6CxRUtwDmilZQ4WIVoPFMY0bchfFqFEnu51rI2JCo7I8XeAtfDZKv4SNMkJ81jZ80KEMST7VLcumPiU2DMXD3r926586BH35aiCs7sZbHKHP6AJkknWqF6DSIv4Sy7k2rRyu8rBiEOieuuW6De57xKFDFs3tjxvCFkKLFVtgW5fIF8VxHRUhXGt2fHSOucVQXMvYIFEmy21pPgREibCTPtDsUb9lqP5OypHw8DumcamU4kwoXp0F8tYert9zKJyM9rLVnRvaDI5goRhEp6sk1SvvolRgvm1rmtNmtuxD7npTCagJ2K4mOSL7MZjuf1IkpXUlp4cCnwibT8UWXgoUt2mOZ35fyYXJc4RVy9ymwufWboFwX1U0c5JHYbk6Kz1DzEZUs6W0s8ag9CUIYUjRsNcWGHygPMfXGwksV7evkLEHbihiDQzHV7jLIDaJG0o8S0WKfCcCqaiCNu22cjwz5MgyiSYPz0cQBMEfGIghcZuL9YVMEkDwMMMrqGZWPem2GNOLl5eaAio70H1qZEZ76vaSkquvPaseMEwe73DAvq25Fg2o05y1yMyI5tobblqUb3Zh2R5sI7RNpVOi0eFWvopkHvMre17uNH9sFfXFTSjG2HWKZkPOKIq32VLbIKb6k9At0ecJRrSqKFRB1pIcuIsYyBuRLCb7NjBHvfGveKfY9G2ePLp2q6SOHOxA7aPppME1cnpn61J0JcqhIBSr9L661wrGzlJjjLYUrYnui41thretBPPXTtoNlLuqEFau21tBvumnpS7qNGPOspD0iMOK3uSZFTemVbONIp4NBuscG14WTyDtChERXmXIQE7tQlRlEJJOi5rLS8JN4yCG9YRa57QyOsPlcGhlIsw4bm4jDratICAAT1TnY2eSmXUscFqrTlCtGZZ5curoDZM8kEItYxqphwDwlftkN5oTmHzz2zmHasV2Hk8L2gHqGRk26nODRzIlJ6nK4B9TeTKymak3DgVku6XY2RIS1pHgtiXRih2IgfJMpNx4Qtgk133SUm7OjNB5veF5CmkjKE52D0icUolq2GG3fARY0zXaKHXOYqtyIT6wDezrP6wFYPVa400tSw4HOpMRDBNOHZzebJkAlwuCjgrXVuw0FUzb3ggcKRZHKaybYwnH2I55mTff1l5gVnoVZ1HNifglUXrPp7mOUPmbflVfRHmjYUYTF9ID2ynEND9DNO3RSUTq0AX1RUbygfAPFQK9Zem3pTJ6P7WUR9nkc2gmrsqEMi3v1rHTTt2omJYW3qUDSpq6xN5DbUCUX8HlAXVf5C7X7AzrYVrWtSFEL59cqblNzYoiy1pEFKp0KNf81SJ1t61N54URSarH7q5MjSaWIBalGemQ5YosO7nJpQgDJsG2h9tcsN4TVF4bT7DF525LP3cQbCgKPhKxGFLo4BCcvyYngo9xU0J3zHTCmjpXbZeKZl1qqzhu8FfH6UDQx3CXzzRUuhO2Ms2S8MwOyxRFs0cBfcUot56UL5fplfWypP8QRnlLw9gFuoR0QoKvmpixB8CovDoQ5Hmyq2oKBCk7CJWv5hMyTC7mBDbHp3YkrfspJqtmSn8DCK0JxOOuYUGMSA1Zt1a1vPDcy4Ol3kq2XL108KlU8pGicmHeE0EhEM7725A1v5f3tU3fjug86QjU71Zk4B5PVq1ZxUXNzGW86qi1jkVFODcRqc6i35q0slvSynaZ5ioA4k76PMpSsTOALVTlif0nfV6U520VjmjT8jQYTkVRVZVSCUsogaoj69vh7KpgL16pfObK0cIIwboqv4XS2J2a2EcxrppALBL5kqqkrGZRJBepo8JFgUxzxTT9y8mcQv0KqxtOTp9NrnTxkIxiaHQKsPEm5tcjBkOkY8w7p1oWn6PgqsbtiVYtZBF7f1j8H81ts2ERmcnUGAf63wlP0HR0TC4uBegMj9nw9cQvYEgORG9zglATAImoZOa56q3MtwEwmleMRE13SzGRmALjlbFVS9I2pbzo4r6yyQviTBS7E6zi0kwj7JYZZuzQhU8NQtgu7SIpl15UBCZBjx9w3Dc0LyCMwxyKAfIF9KgqeEW0BJEKfSFRrpbKbaVtTH9nS6sauAZXUS5t7FTMmx5RZt1NxX1Br1kfJsb467Sz4oUDCyu8Gy43nbEqkVF0VE2IKQb6GVxFF3qqche0YhGPK9HtCDA1L5VxpL5tsGoDrbaGxf072ZsiTBBIsoJUUglBzoc0gUJfrMAQVHeBw1MyleWkEQDN9PJ6lISxWJmhXkrVO7agKTqgRa5FJMXBILtQ5RgrR78qCByDnUU2YJni8jZjf4voW6AOPI8xNb9rJVWMpkiEN7RGNCmha0hXo73XCKkcYNNwVtW2uDfCLXL0x7UALSPx3vanx6SMuyiV11MLrElosI6HGK3ZtEZVU3bxD",
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes name that excedes 50 char limit
    def test_createImageBadData019(self):
        module_logger.info('Start test_createImageBadData019')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": "ainMsStJ2NuziqVSZkE2Mfh7uBPy12cn5Vj2MJcN2xCmWKpenSf",
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes name that is int
    def test_createImageBadData020(self):
        module_logger.info('Start test_createImageBadData020')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": 1138,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes width that is string
    def test_createImageBadData021(self):
        module_logger.info('Start test_createImageBadData021')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":"fakewidth",
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes width that excedes max value
    def test_createImageBadData022(self):
        module_logger.info('Start test_createImageBadData022')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":8388608,
                           "height":self.testHeight,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes height that excedes max value
    def test_createImageBadData023(self):
        module_logger.info('Start test_createImageBadData023')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":8388608,
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes height that is string
    def test_createImageBadData024(self):
        module_logger.info('Start test_createImageBadData024')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":"8388608",
                           "type":self.testType
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes bad type string
    def test_createImageBadData025(self):
        module_logger.info('Start test_createImageBadData025')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":".jpg"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 2 of the same attribute (type)
    # each have same valid value
    def test_createImageBadData026(self):
        module_logger.info('Start test_createImageBadData026')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"jpg",
                           "type":"jpg"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 2 of the same attribute (type)
    # each has unique valid value
    def test_createImageBadData027(self):
        module_logger.info('Start test_createImageBadData027')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"jpg",
                           "type":"png"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 2 of the same attribute (type)
    # first is invalid second is valid
    def test_createImageBadData028(self):
        module_logger.info('Start test_createImageBadData028')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":".jpg",
                           "type":"png"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 2 of the same attribute (type)
    # first is valid second is invalid
    def test_createImageBadData029(self):
        module_logger.info('Start test_createImageBadData029')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"png",
                           "type":".jpg"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 2 of the same attribute (type) non-sequentially
    # first is invalid second is valid
    def test_createImageBadData030(self):
        module_logger.info('Start test_createImageBadData030')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "type":".jpg",
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"png",
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 2 of the same attribute (type) non-sequentially
    # first is valid second is invalid
    def test_createImageBadData031(self):
        module_logger.info('Start test_createImageBadData031')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "type":"jpg",
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":".png",
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 4 of the same attribute (type)
    # ends sequence w/bad
    def test_createImageBadData032(self):
        module_logger.info('Start test_createImageBadData032')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"png",
                           "type":".jpg",
                           "type":"png",
                           "type":".jpg"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
          
    # passes the 5 required attributes in payload 
    # includes 4 of the same attribute (type)
    # ends sequence w/good
    def test_createImageBadData033(self):
        module_logger.info('Start test_createImageBadData033')
                      
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                
        # data to be used in post
        imgData = json.dumps({"images":[{"url": self.testUrl,
                           "name": self.testName,
                           "width":self.testWidth,
                           "height":self.testHeight,
                           "type":"png",
                           "type":".jpg",
                           "type":"png",
                           "type":"jpg"
                         }]})
                  
        # posts data and returns response 
        response = self.postImage(project_id, user_id, 
                   token, serviceUrl = self.serviceUrl, 
                   data = imgData )
               
        # checks response
        self.responseCheck01(response, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, new_id was None and message was "not found"', 
                             failMsg = 'FAIL : status code was not 400')
        