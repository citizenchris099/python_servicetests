"""
tests the image_repo Deleteimage function
"""
import logging
import json
module_logger = logging.getLogger('testlogger')

from ImageManagerTests import imageManagerTests

class deleteImageTests(imageManagerTests):

    
    # tests Hard Deleting an image 
    def test_hardDeleteImage001(self):
        module_logger.info('Start test_hardDeleteImage001')
                    
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # creates new image      
        imgID, _ = self.createImage01(project_id, user_id, token)
        
        response = self.successful_delete02(imgID, project_id, user_id, token)
        
        self.assertEquals(response.status_code, 200)
        message = self.delResponseMessage(response)
        self.assertEquals(message, "OK")
        module_logger.info('PASS: Image was deleted')
        
    # tests Hard Deleting an image w/bad token
    def test_hardDeleteImageBadToken(self):
        module_logger.info('Start test_hardDeleteImageBadToken')
                    
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # creates new image      
        imgID, _ = self.createImage01(project_id, user_id, token)
        
        response = self.successful_delete02(imgID, project_id, user_id, "xxx")
        
        self.assertEquals(response.status_code, 401)
        message = self.delResponseMessage(response)
        self.assertEquals(message, "Unauthorized")
        module_logger.info('PASS: Image was not deleted')
        
    # tests Hard Deleting an image w/bad proj id
    def test_hardDeleteImageBadProjID(self):
        module_logger.info('Start test_hardDeleteImageBadProjID')
                    
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # creates new image      
        imgID, _ = self.createImage01(project_id, user_id, token)
        
        response = self.successful_delete02(imgID, "xxx", user_id, token)
        
        self.assertEquals(response.status_code, 401)
        message = self.delResponseMessage(response)
        self.assertEquals(message, "Unauthorized")
        module_logger.info('PASS: Image was not deleted')
        
    # tests Hard Deleting an image w/bad proj id
    def test_hardDeleteImageBadUsrID(self):
        module_logger.info('Start test_hardDeleteImageBadUsrID')
                    
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # creates new image      
        imgID, _ = self.createImage01(project_id, user_id, token)
        
        response = self.successful_delete02(imgID, project_id, "xxx", token)
        
        self.assertEquals(response.status_code, 401)
        message = self.delResponseMessage(response)
        self.assertEquals(message, "Unauthorized")
        module_logger.info('PASS: Image was not deleted')
        
    # tests soft deleting image
    # ensure you can't get image once soft deleted (include_deleted=false)
    def test_softDelete001(self):
        module_logger.info('Start test_updateImage001')
                    
        # gets auth info
        project_id, user_id, token = self.get_token_data(uName = self.enfAdmU, 
                                                          pWord = self.enfAdmP,
                                                         listInt = 1) 
        
        # creates new image      
        imgID, _ = self.createImage01(project_id, user_id, token)
        
        patchData = json.dumps({"deleted":True
                                })
        
        # updates the above created image
        response2 = self.patchImage(project_id, user_id, 
                          token, serviceUrl = self.getUrl, 
                          data = patchData, 
                          image_id = imgID)
        
        # checks response 
        self.responseCheck02(response2, "deleted", 1, 0, 200, "new image patched")
        
        # tries to get image with include_deleted=false
        response3 = self.serviceGet03(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        
        self.assertEquals(response3.status_code, 404)
        _, message = self.getResponseMessage(response3)
        self.assertEquals(message, "Not Found")
        module_logger.info('PASS: Image was not soft deleted')
        
        
                    