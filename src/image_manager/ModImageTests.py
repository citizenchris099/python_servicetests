"""
tests the image_repo Modify image function
"""
import logging
import json
import requests
import time
module_logger = logging.getLogger('testlogger')

from ImageManagerTests import imageManagerTests

class modImageTests(imageManagerTests):

    
    # basic test of image_repo mod image function
    # asserts that the child image has the correct mod values
    def test_modImage001(self):
        module_logger.info('Start test_modImage001')
                         
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
             
        # creates new parent image      
        imgID, _ = self.createImage02(project_id, user_id, token,
                                      self.testUrl)
             
        # data used for modifying image
        modData = json.dumps({"input_id": str(imgID),
                              "modifications" :
                                {    
                                 "width":self.modWidth,
                                 "height":self.modHeight
                                 }  
                              })
             
        # creates child image aka modifies parent image
        # gets task id and task status
        _, response5 = self.modParentImage01(project_id, user_id, token, modData)
             
        # validates child image contains above modified values
        self.assertEquals(response5.status_code, 200)
        _, message = self.getResponseMessage(response5, key="width")
        self.assertEquals(message, self.modWidth)
        _, message = self.getResponseMessage(response5, key="height")
        self.assertEquals(message, self.modHeight)
        _, message = self.getResponseMessage(response5, key="parent")
        self.assertEquals(message, imgID)
        module_logger.debug(response5)
        module_logger.info('PASS: child image retrieved and w/h values have been modified')
#            
#         
#     # similar to the above test
#     # adds a hard delete to the parent image
#     # tests whether this in fact deletes both parent child
#     def test_modImage002(self):
#         module_logger.info('Start test_modImage002')
#                          
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#              
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       self.testUrl)
#              
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "width":self.modWidth,
#                                  "height":self.modHeight
#                                  }  
#                               })
#              
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         message2, response5 = self.modParentImage01(project_id, user_id, token, modData)
#              
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         _, message = self.getResponseMessage(response5, key="width")
#         self.assertEquals(message, self.modWidth)
#         _, message = self.getResponseMessage(response5, key="height")
#         self.assertEquals(message, self.modHeight)
#         module_logger.debug(response5)
#         module_logger.info('child image retrieved and w/h values have been modified')
#                  
#         # deletes parent image
#         self.hardDeleteParentImage01(imgID)
#               
#         # attempts to retrieve the child image   
#         # this should fail due to the parent image having been deleted
#         response = self.getChildImage01(project_id, user_id, token, 
#                                              modurl = message2)
#      
#         self.assertEquals(response.status_code, 404)
#         _, message = self.getResponseMessage(response)
#         self.assertEquals(message, "Not Found")
#         module_logger.debug(response)
#         module_logger.info("PASS: child image was deleted along w/parent image")
#            
#     # tests that modding the strip option
#     def test_modImage003(self):
#         module_logger.info('Start test_modImage003')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/strip/Brainy.jpg")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "strip":True
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: meta data was stripped')
#            
#     # tests that modding the flatten option
#     def test_modImage004(self):
#         module_logger.info('Start test_modImage004')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/flatten/Brainy.png")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "flatten":False
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was flattened')
#            
#     # tests that modding the correct_gamma option
#     def test_modImage005(self):
#         module_logger.info('Start test_modImage005')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/correct_gamma/Brainy.jpg")
#    
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "correct_gamma":True
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was flattened')
#            
#     # tests that modding the quality option
#     def test_modImage006(self):
#         module_logger.info('Start test_modImage006')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/quality/Brainy.jpg")
#    
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "quality":100
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was flattened')
#            
#     # tests that modding the background option (hexadecimal code)
#     def test_modImage007(self):
#         module_logger.info('Start test_modImage007')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/background/Brainy.png")
#             
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "background":"#FFC1C1"
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#            
#     # tests that modding the background option (name)
#     def test_modImage008(self):
#         module_logger.info('Start test_modImage008')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/background/Brainy.png")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "background":"RosyBrown1"
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#           
#     # tests that modding the resize_strategy option (stretch)
#     def test_modImage009(self):
#         module_logger.info('Start test_modImage009')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/resize_strategy/stretch/Brainy.jpg")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "resize_strategy":"stretch",
#                                  "width":400,
#                                  "height":200
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#           
#     # tests that modding the resize_strategy option (pad)
#     def test_modImage010(self):
#         module_logger.info('Start test_modImage010')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/resize_strategy/pad/Brainy.jpg")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "resize_strategy":"pad",
#                                  "width":400,
#                                  "height":200
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#           
#     # tests that modding the resize_strategy option (crop)
#     def test_modImage011(self):
#         module_logger.info('Start test_modImage011')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/resize_strategy/crop/Brainy.jpg")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "resize_strategy":"crop",
#                                  "x1":80,
#                                  "y1":100,
#                                  "x2":160,
#                                  "y2":180,
#                                  "gravity":"bottom-right",
#                                  "zoom":False,
#                                  "width":100,
#                                  "height":100
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#           
#     # tests that modding the resize_strategy option (fillcrop)
#     def test_modImage012(self):
#         module_logger.info('Start test_modImage012')
#                          
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#              
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/resize_strategy/fillcrop/Brainy.jpg")
#             
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "resize_strategy":"fillcrop",
#                                  "width":200,
#                                  "height":150
#                                  }  
#                               })
#              
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#              
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#           
#     # tests that modding the format option (jpg)
#     def test_modImage013(self):
#         module_logger.info('Start test_modImage013')
#                          
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#              
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/format/jpg/Brainy.png")
#             
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "format":"jpg"
#                                  }  
#                               })
#              
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#              
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         _, message = self.getResponseMessage(response5, key="type")
#         self.assertEquals(message, "jpg")
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#           
#     # tests that modding the format option (png)
#     def test_modImage014(self):
#         module_logger.info('Start test_modImage014')
#                          
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#              
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/format/png/Brainy.jpg")
#             
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "format":"png"
#                                  }  
#                               })
#              
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#              
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         _, message = self.getResponseMessage(response5, key="type")
#         self.assertEquals(message, "png")
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image background was modified')
#          
#     # tests that modding the format option (gif)
#     def test_modImage015(self):
#         module_logger.info('Start test_modImage015')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/format/gif/Brainy.jpg")
#            
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "format":"gif"
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         _, message = self.getResponseMessage(response5, key="type")
#         self.assertEquals(message, "gif")
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image format was modified to gif')
#          
#     # tests that modding the format option (tiff)
#     def test_modImage016(self):
#         module_logger.info('Start test_modImage016')
#                           
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#               
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/format/tiff/Brainy.jpg")
#              
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "format":"tiff"
#                                  }  
#                               })
#               
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#               
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         _, message = self.getResponseMessage(response5, key="type")
#         self.assertEquals(message, "tiff")
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image format was modified to gif')
#          
#     # tests that modding the format option (tiff) from a .gif
#     def test_modImage017(self):
#         module_logger.info('Start test_modImage017')
#                           
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#               
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/format/tiff/Dazed_Papa_Smurf.gif")
#              
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {  
#                                  "force_accept":True, 
#                                 "frame":1,  
#                                 "format":"tiff"
#                                  }  
#                               })
#               
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#               
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         _, message = self.getResponseMessage(response5, key="type")
#         self.assertEquals(message, "tiff")
#         module_logger.debug(response_data)
#         module_logger.info('PASS: gif format was modified to gif')
#          
#     # a copy of test_modImage001
#     # the only change being the url points to a gif 
#     def test_modImage018(self):
#         module_logger.info('Start test_modImage018')
#                         
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#             
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/Dazed_Papa_Smurf.gif")
#             
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "width":self.modWidth,
#                                  "height":self.modHeight
#                                  }  
#                               })
#             
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#             
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         _, message = self.getResponseMessage(response5, key="width")
#         self.assertEquals(message, self.modWidth)
#         _, message = self.getResponseMessage(response5, key="height")
#         self.assertEquals(message, self.modHeight)
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response5)
#         module_logger.info('PASS: gif image retrieved and w/h values have been modified')
#          
#     # tests that modding the colorspace (sRGB)
#     def test_modImage019(self):
#         module_logger.info('Start test_modImage019')
#                            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/scRGB/Brainy.jpg")
#               
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"sRGB"
#                                  }  
#                               })
#                
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to sRGB')
#          
#     # tests that modding the colorspace (CMY)
#     def test_modImage020(self):
#         module_logger.info('Start test_modImage020')
#                            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/CMY/Brainy.jpg")
#               
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"CMY"
#                                  }  
#                               })
#                
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to CMY')
#          
#     # tests that modding the colorspace (CMYK)
#     def test_modImage021(self):
#         module_logger.info('Start test_modImage021')
#                            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/CMYK/Brainy.jpg")
#               
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"CMYK"
#                                  }  
#                               })
#                
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to CMYK')
#          
#     # tests that modding the colorspace (Gray)
#     def test_modImage022(self):
#         module_logger.info('Start test_modImage022')
#                            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/Gray/Brainy.jpg")
#               
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"Gray"
#                                  }  
#                               })
#                
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to Gray')
#          
#     # tests that modding the colorspace (RGB)
#     def test_modImage023(self):
#         module_logger.info('Start test_modImage022')
#                            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/RGB/Brainy.jpg")
#               
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"RGB"
#                                  }  
#                               })
#                
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to RGB')
#          
#     # tests that modding the colorspace (scRGB)
#     def test_modImage024(self):
#         module_logger.info('Start test_modImage024')
#                            
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/scRGB/Brainy.jpg")
#               
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"scRGB"
#                                  }  
#                               })
#                
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to scRGB')
#          
#     # tests that modding the colorspace (Transparent)
#     def test_modImage025(self):
#         module_logger.info('Start test_modImage025')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/colorspace/Transparent/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "colorspace":"Transparent"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image colorspace was modified to Transparent')
#          
#     # tests that modding the sepia
#     def test_modImage026(self):
#         module_logger.info('Start test_modImage026')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/sepia/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "sepia":50
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was modified to sepia')
#          
#     # tests that modding the rotation set to false
#     def test_modImage027(self):
#         module_logger.info('Start test_modImage027')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/rotation/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "rotation":False
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image rotation was set to false')
#          
#     # tests that modding the rotation set to degrees
#     def test_modImage028(self):
#         module_logger.info('Start test_modImage028')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/rotation/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "rotation":90
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was rotated')
#          
#     # tests that modding the compress setting (BZip)
#     def test_modImage029(self):
#         module_logger.info('Start test_modImage029')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/BZip/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"BZip"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using BZip')
#          
#     # tests that modding the compress setting (Fax)
#     def test_modImage030(self):
#         module_logger.info('Start test_modImage030')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/Fax/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"Fax"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using Fax ')
#          
#     # tests that modding the compress setting (Group4)
#     def test_modImage031(self):
#         module_logger.info('Start test_modImage031')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/Group4/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"Group4"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using Group4 ')
#          
#     # tests that modding the compress setting (JPEG)
#     def test_modImage032(self):
#         module_logger.info('Start test_modImage032')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/JPEG/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"JPEG"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using JPEG ')
#          
#     # tests that modding the compress setting (JPEG2000)
#     def test_modImage033(self):
#         module_logger.info('Start test_modImage032')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/JPEG2000/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"JPEG2000"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using JPEG2000 ')
#          
#     # tests that modding the compress setting (Lossless)
#     def test_modImage034(self):
#         module_logger.info('Start test_modImage034')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/Lossless/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"Lossless"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using Lossless ')
#          
#     # tests that modding the compress setting (LZW)
#     def test_modImage035(self):
#         module_logger.info('Start test_modImage035')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/LZW/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"LZW"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using LZW ')
#          
#     # tests that modding the compress setting (RLE)
#     def test_modImage036(self):
#         module_logger.info('Start test_modImage036')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/RLE/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"RLE"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using RLE ')
#          
#     # tests that modding the compress setting (Zip)
#     def test_modImage037(self):
#         module_logger.info('Start test_modImage037')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/compress/Zip/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "compress":"Zip"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was compressed using Zip ')
#          
#     # tests that modding the blur setting
#     def test_modImage038(self):
#         module_logger.info('Start test_modImage038')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/blur/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "blur":"5x0.5"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image was blurred ')
#          
#     # tests that modding the text setting
#     def test_modImage039(self):
#         module_logger.info('Start test_modImage039')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/text/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "text": [
#                                           {
#                                            "text": "Example text",
#                                            "size": 12,
#                                            "valign": "top"
#                                             },
#                                           {
#                                            "text": "Another example text",
#                                            "size": 10,
#                                            "valign": "bottom"
#                                            }
#                                           ]
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image text was added ')
#          
#     # tests that modding the progressive setting
#     def test_modImage040(self):
#         module_logger.info('Start test_modImage040')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/progressive/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "progressive":True
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image progressive setting modified ')
#          
#     # tests that modding the transparent setting
#     def test_modImage041(self):
#         module_logger.info('Start test_modImage041')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/transparent/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "transparent":"RoyalBlue"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image transparent setting modified ')
#          
#     # tests that modding the clip setting
#     def test_modImage042(self):
#         module_logger.info('Start test_modImage042')
#                              
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                  
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/clip/Brainy.jpg")
#                 
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "clip":True
#                                  }  
#                               })
#                  
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                  
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image clip setting modified ')
#          
#     # tests that modding the negate setting
#     def test_modImage043(self):
#         module_logger.info('Start test_modImage043')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/negate/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "negate":True
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image negate setting modified ')
#          
#     # tests that modding the density setting
#     def test_modImage044(self):
#         module_logger.info('Start test_modImage044')
#                             
#         # gets auth info
#         project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
#                                                           pWord = self.enfAdmP,
#                                                          listInt = 1) 
#                 
#         # creates new parent image      
#         imgID, _ = self.createImage02(project_id, user_id, token,
#                                       "/home/chris/Pictures/image-repo/smurfs/density/Brainy.jpg")
#                
#         # data used for modifying image
#         modData = json.dumps({"input_id": str(imgID),
#                               "modifications" :
#                                 {    
#                                  "density":"400"
#                                  }  
#                               })
#                 
#         # creates child image aka modifies parent image
#         # gets task id and task status
#         _, response5 = self.modParentImage01(project_id, user_id, token, modData)
#                 
#         # validates child image contains above modified values
#         self.assertEquals(response5.status_code, 200)
#         response_data = response5.json()
#         _, message = self.getResponseMessage(response5, key="parent")
#         self.assertEquals(message, imgID)
#         module_logger.debug(response_data)
#         module_logger.info('PASS: image density setting modified ')
        
    # similar to test_modImage002
    # attempts to hard delete to the child image
    # this should fail
    def test_modImage045(self):
        module_logger.info('Start test_modImage002')
                         
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
             
        # creates new parent image      
        imgID, _ = self.createImage02(project_id, user_id, token,
                                      self.testUrl)
             
        # data used for modifying image
        modData = json.dumps({"input_id": str(imgID),
                              "modifications" :
                                {    
                                 "width":self.modWidth,
                                 "height":self.modHeight
                                 }  
                              })
             
        # creates child image aka modifies parent image
        # gets task id and task status
        _, response5 = self.modParentImage01(project_id, user_id, token, modData)
             
        # validates child image contains above modified values
        self.assertEquals(response5.status_code, 200)
        _, message = self.getResponseMessage(response5, key="width")
        self.assertEquals(message, self.modWidth)
        _, message = self.getResponseMessage(response5, key="height")
        self.assertEquals(message, self.modHeight)
        _, message = self.getResponseMessage(response5, key="parent")
        self.assertEquals(message, imgID)
        module_logger.debug(response5)
        module_logger.info('child image retrieved and w/h values have been modified')
        
        # child image id
        _, message = self.getResponseMessage(response5, key="id")
        module_logger.debug(message)
                 
        # deletes child image
        response = self.successful_delete(message, self.enfAdmU, 
                                              self.enfAdmP, 1)

        self.assertEquals(response.status_code, 400)
        message = self.delResponseMessage(response)
        self.assertEquals(message, "Bad Request")
        response_data = response.json()
        module_logger.debug(response_data)
        module_logger.info("PASS: Child Image was not deleted and delete attempt returned 400")
         
    # tests that modding the force_accept setting
    # sending bad format
    def test_badModImage001(self):
        module_logger.info('Start test_badModImage001')
                              
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                  
        # creates new parent image      
        imgID, _ = self.createImage02(project_id, user_id, token,
                                      "/home/chris/Pictures/image-repo/smurfs/force_accept/The_Smurfs_intro.mp4")
                 
        # data used for modifying image
        modData = json.dumps({"input_id": str(imgID),
                              "modifications" :
                                {    
                                 "force_accept":True
                                 }  
                              })
                  
        # creates child image aka modifies parent image
        # gets task id and task status
        _, response5 = self.modParentImage01(project_id, user_id, token, modData)
                  
        # validates child image contains above modified values
        self.assertEquals(response5.status_code, 200)
        response_data = response5.json()
        _, message = self.getResponseMessage(response5, key="parent")
        self.assertEquals(message, imgID)
        module_logger.debug(response_data)
        module_logger.info('PASS: image force_accept setting modified ')
          
    # sending bad mod request
    def test_badModImage002(self):
        module_logger.info('Start test_badModImage002')
                              
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
                  
        # creates new parent image      
        imgID, _ = self.createImage02(project_id, user_id, token,
                                      "/home/chris/Pictures/image-repo/smurfs/bad/Brainy.jpg")
                 
        # data used for modifying image
        modData = json.dumps({"input_id": str(imgID),
                              "modifications" :
                                {    
                                 "the_force":"is strong with this one"
                                 }  
                              })
                  
        # creates child image aka modifies parent image
        # gets task id and task status
        _, response5 = self.modParentImage01(project_id, user_id, token, modData)
                  
        # validates child image contains above modified values
        self.assertEquals(response5.status_code, 200)
        response_data = response5.json()
        _, message = self.getResponseMessage(response5, key="parent")
        self.assertEquals(message, imgID)
        module_logger.debug(response_data)
        module_logger.info('PASS: image force_accept setting modified ')
         
    # attempts to soft delete parent image while child still present (not hard deleted)
    def test_modImage046(self):
        module_logger.info('Start test_modImage045')
                        
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
            
        # creates new parent image      
        imgID, _ = self.createImage02(project_id, user_id, token,
                                      self.testUrl)
            
        # data used for modifying image
        modData = json.dumps({"input_id": str(imgID),
                              "modifications" :
                                {    
                                 "width":self.modWidth,
                                 "height":self.modHeight
                                 }  
                              })
            
        # creates child image aka modifies parent image
        # gets task id and task status
        _, response5 = self.modParentImage01(project_id, user_id, token, modData)
            
        # validates child image contains above modified values
        self.assertEquals(response5.status_code, 200)
        _, message = self.getResponseMessage(response5, key="width")
        self.assertEquals(message, self.modWidth)
        _, message = self.getResponseMessage(response5, key="height")
        self.assertEquals(message, self.modHeight)
        _, message = self.getResponseMessage(response5, key="parent")
        self.assertEquals(message, imgID)
        module_logger.debug(response5)
        module_logger.info('child image retrieved and w/h values have been modified')
         
        patchData = json.dumps({"deleted":True
                                })
           
        # updates the above created image
        response1 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
         
        # tries to get image with include_deleted=false
        response2 = self.serviceGet03(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
         
        _, message2 = self.getResponseMessage(response2, "url")
        self.assertEquals(message2, self.testUrl)
           
        # checks the response of the patch 
        self.responseCheck01(response1, code = 400, 
                             expected = "Bad Request", 
                             passMsg = 'PASS : status code was 400, and message was "Bad Request"', 
                             failMsg = 'FAIL : status code was not 400')

        
            
    # used validate mods
    def getTaskId01(self, project_id, user_id, token, response,
                        key, listInt,
                        ):
        if response.status_code == 202:
            response_data = response.json()
            module_logger.debug(response_data)
            new_id, _ = self.postResponseMessage(response, listInt, key)
            self.assertIsNotNone(new_id)

            return new_id
        elif response.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response)
            self.fail('status code was 500')
        else:
            response_data = response.json()
            module_logger.debug(response_data)
            module_logger.info('FAIL : status code was not 202')
            module_logger.debug("status code was")
            module_logger.debug(response.status_code)
            self.fail('status code was not 202')

    
    
    # used in mod image tests
    # when async task status is still processing (or 200)
    def getChildImageId(self, project_id, user_id, token, serviceUrl, imgid, response, response_data):
        
                               
        tryCount = 0

        while tryCount < 10:
            code = response.status_code 
            if code == 201:
                message = response_data["links"][1]["href"]
                module_logger.debug(message)
                module_logger.info('transloadit processing complete')
                return message
            elif code == 500:
                module_logger.info('FAIL : Transloadit could not complete. status code was 500')
                module_logger.debug(response)
                self.fail('FAIL : Transloadit could not complete. status code was 500')

            else:
                # try again
                time.sleep(10)
                response = self.serviceGet02(project_id, user_id, 
                          token, serviceUrl, 
                          imgid)
                response_data = response.json()
        
            tryCount += 1
            
        # fail
        self.fail("Timeout after 10 tries")
        module_logger.info('FAIL : Timeout after 10 tries')
        
    # uses the child image url to get the child image
    def getChildImage01(self, project_id, user_id, token, modurl):
        
        response = requests.get(url=modurl, 
                                headers=self.basicHeaderInfo(
                                project_id, user_id, token))
        
        return response
    
    def modParentImage01(self, project_id, user_id, token, modData):
        response2 = self.postImage(project_id, user_id, token, self.serviceUrl, 
            modData)
        
        if response2.status_code == 202:
            response_data = response2.json()
            module_logger.info('parent image modified')
            module_logger.debug(response_data)
        
            # gets the task id
            taskId = self.getTaskId01(project_id, user_id, token, 
                             response2,key = None,
                            listInt = None)
        
            # gets the task status    
            response3 = self.serviceGet02(project_id, user_id, 
                          token, serviceUrl = self.asyncTaskUrl, 
                          image_id = taskId)
            
            response_data2 = response3.json()
            
            module_logger.info('transloadit task id retrieved')
            module_logger.debug(response_data2)
        
            # loops until the transloadit task is complete 
            message2 = self.getChildImageId(project_id, 
                                         user_id, token, 
                                         self.asyncTaskUrl, 
                                         taskId,
                                         response3,
                                         response_data2)
        
            # once transloadit task complete should now have child image url
            # with the child image url we can retrieve child image   
            response5 = self.getChildImage01(project_id, user_id, token, 
                                             modurl = message2)
            
            return message2, response5
        
        elif response2.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response2)
            self.fail('status code was 500')
        else:
            response_data = response2.json()
            module_logger.debug(response_data)
            module_logger.info('FAIL: parent image was not modified. status code was not 202')
            module_logger.debug("status code was")
            module_logger.debug(response2.status_code)
            self.fail('status code was not 202')
            
            
    def hardDeleteParentImage01(self, imgID):
        
        response = self.successful_delete(imgID, self.enfAdmU, 
                                              self.enfAdmP, 1)
        if response.status_code == 200: 
            response_data = response.json()   
            message = self.delResponseMessage(response)
            self.assertEquals(message, "OK")
            module_logger.info('parent image deleted')
            module_logger.debug(response_data)
        elif response.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response)
            self.fail('status code was 500')
        else:
            response_data = response.json()
            module_logger.debug(response_data)
            module_logger.info('FAIL : parent image not deleted. status code was not 200')
            module_logger.debug("status code was")
            module_logger.debug(response.status_code)
            self.fail('status code was not 200')

