"""
parent class for all Image Repo tests
"""

import json
import unittest
import requests
import logging
module_logger = logging.getLogger('testlogger')


class imageManagerTests(unittest.TestCase):
    
    added_imageIds = []

    def setUp(self):
        
        module_logger.info('Test Begun')
        
        self.wrapper_url = 'http://127.0.0.1:5000'
        self.enfold_url = 'http://dall-keys-web02.balfour.corp:8000'
        self.serviceUrl = '{0:s}/api_1_0/images'
        self.getUrl = '{0:s}/api_1_0/images/'
        self.blobUrl = '{0:s}/api_1_0/images/blob/'
        self.getUsrUrl = '{0:s}/api_1_0/images/users/'
        self.getProUrl = '{0:s}/api_1_0/images/projects/'
        self.getNamUrl = '{0:s}/api_1_0/images?name='
        self.asyncTaskUrl = '{0:s}/api_1_0/tasks/'
        self.enfAdmU = 'veggie_smurf'
        self.enfAdmP = 'meatisevil'
        self.enfAdvU = 'VeggieAdviser'
        self.enfAdvP = 'tofuisgreat'
        self.testUrl = "smurfs/Brainy.jpg"
        self.testName = "Brainy Smurf"
        self.testWidth = 200
        self.testHeight = 200
        self.testType = "jpg"
        self.modWidth = 400
        self.modHeight = 400
        
                
    def tearDown(self):
        
        uName = "veggie_smurf"
        pWord = "meatisevil"
        listInt = 1
        
        module_logger.info('Test Complete')
        
        # clean up
        for imageId in self.added_imageIds:
            if imageId is not None:
                self.successful_delete(imageId, uName, pWord, listInt)
                
#     def test_imageCleanUp(self):
#         uName = "veggie_smurf"
#         pWord = "meatisevil"
#         listInt = 1
#             
#         imageIds = [298,299,300,301]
#         for imageId in imageIds:
#             if imageId is not None:
#                 self.successful_delete(imageId, uName, pWord, listInt)      
        
        
    # retrieves token data from enfold api    
    def get_token_data(self, uName, pWord, listInt):
        
        data = dict()
        data['username'] = uName
        data['password'] = pWord 
         
        header = dict()
        header['content-type'] = 'application/json'
        
        post_json = json.dumps(data)
        post_url = "{0:s}/authenticate".format(self.enfold_url)
        
        # uses all the data to connect to the api
        response = requests.post(
            url=post_url,
            headers=header,
            data=post_json)
        
        response_data = response.json()
        assert response.status_code == 200
        
        project_id = response_data["projects"][listInt]["id"]
        user_id = response_data["token"]["user"]["id"]
        token = response_data["token"]['x-subject-token']
        return project_id, user_id, token
    
    # deletes an image from the db outside the context of a test
    def successful_delete(self, image_id, uName, pWord, listInt):
        
        # gets the above token data
        project_id, user_id, token = self.get_token_data(uName, pWord, listInt)
        
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = self.getUrl.format(self.wrapper_url) + str(image_id)
        
        # uses all the data to connect to the api
        response = requests.delete(url=post_url, headers=header)
        
        # checks response
        return response
    
    def successful_delete02(self, image_id, project_id, user_id, token):
        
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = self.getUrl.format(self.wrapper_url) + str(image_id)
        
        # uses all the data to connect to the api
        response = requests.delete(url=post_url, headers=header)
        
        # checks response
        return response
    
    # used to Get Info about students
    def serviceGet01(self, project_id, user_id, 
                     token, serviceUrl,
                     image_id):
        
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = serviceUrl.format(self.wrapper_url) + str(image_id)
        
        # uses all the data to connect to the api
        response = requests.get(url=post_url, 
                                headers=header)
        
        return response
    
    # used to Get Info about students
    def serviceGet02(self, project_id, user_id, 
                     token, serviceUrl,
                     image_id):
        
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = serviceUrl.format(self.wrapper_url) + str(image_id)+"?include_deleted=true"
        
        # uses all the data to connect to the api
        response = requests.get(url=post_url, 
                                headers=header)
        
        return response
    
    # used to Get Info about students
    def serviceGet03(self, project_id, user_id, 
                     token, serviceUrl,
                     image_id):
        
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = serviceUrl.format(self.wrapper_url) + str(image_id)+"?include_deleted=false"
        
        # uses all the data to connect to the api
        response = requests.get(url=post_url, 
                                headers=header)
        
        return response
    
    
    def postImage(self, project_id, user_id, 
                  token, serviceUrl, 
                  data):
                
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = serviceUrl.format(self.wrapper_url)
        
        # uses all the data to connect to the api
        response = requests.post(
            url=post_url,
            headers=header,
            data=data)
                        
        
        return response
    
    
    
    def patchImage(self, project_id, user_id, 
                  token, serviceUrl, 
                  data, image_id):
                
        # header info
        header = self.basicHeaderInfo(project_id, user_id, token)
        
        # appends the correct info to the wrapper url
        post_url = serviceUrl.format(self.wrapper_url)+ str(image_id)
        
        # uses all the data to connect to the api
        response = requests.patch(
            url=post_url,
            headers=header,
            data=data)
                        
        
        return response
    
        
    # checks the json response messages for the varoius methods and return payloads
    def delResponseMessage(self, response):
        response_data = response.json()
        message = response_data["status"]
        module_logger.debug(response_data)
        return message
    
    def patchResponseMessage(self, response, expected, key):
        response_data = response.json()
        if response.status_code == 200:
            message = response_data["images"][0][key]
        else: 
            message = response_data["status"]
            
        return message
        
    def postResponseMessage(self, response, listInt, key):
        
        if response.status_code == 201:
            response_data = response.json()
            message = response_data["images"][listInt][key]
            new_id = response_data["images"][listInt]["id"]
            
        elif response.status_code == 200:
            response_data = response.json()
            message = response_data["images"][listInt][key]
            new_id = response_data["images"][listInt]["id"]
            
        elif response.status_code == 202:
            response_data = response.json()
            message = None
            new_id = response_data["task_id"]
            
        else: 
            response_data = response.json()
            message = response_data["status"]
            new_id = None
    
        return new_id, message
    
    def getResponseMessage(self, response, key = None):
        response_data = response.json()
        if response.status_code == 200:
            message = response_data[key]
            new_id = response_data["id"]
            
        else: 
            message = response_data["status"]
            new_id = None
            
        return new_id, message
    
    # creates a student record w/the minimum 5 attributes required
    def createImage01(self, project_id, user_id, token):
        # data to be used in post
        imgData = json.dumps({"images":[{"url":self.testUrl, "name":self.testName, 
                        "width":self.testWidth, 
                        "height":self.testHeight, 
                        "type":self.testType}]})
        # posts data and returns response
        response = self.postImage(project_id, user_id, token, serviceUrl=self.serviceUrl, 
            data=imgData)
        
        # checks response
        imgID = self.responseCheck02(response, key="url", 
            expected=self.testUrl, 
            listInt=0, 
            code=201, 
            logMsg='new image created')
        
        # attempts to Get / Read the newly created Student Record
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image retrieved from db')
        self.added_imageIds.append(imgID)
        return imgID, response2
    
    # creates a student record w/the minimum 5 attributes required
    # requires url (used in Mod tests)
    def createImage02(self, project_id, user_id, token,url):
        
        # data to be used in post
        imgData = json.dumps({"images":[{"url":url, 
                                         "name":self.testName, 
                                         "width":self.testWidth, 
                                         "height":self.testHeight, 
                                         "type":self.testType}]})
        
        # posts data and returns response
        response = self.postImage(project_id, user_id, 
                                  token, serviceUrl=self.serviceUrl, 
                                  data=imgData)
        
        # checks response
        imgID = self.responseCheck02(response,"url", 
            url, 
            listInt=0, 
            code=201, 
            logMsg='new image created')
        
        # attempts to Get / Read the newly created Student Record
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image retrieved from db')
        
                
        module_logger.info('parent image created')
        self.added_imageIds.append(imgID)
        return imgID, response2
    
    # creates 2 student records w/the minimum 5 attributes required
    def createImage03(self, project_id, user_id, token):
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
        
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID1)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image 1 retrieved from db')
        
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID2)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image 2 retrieved from db')
        self.added_imageIds.append(imgID1)
        self.added_imageIds.append(imgID2)
        return imgID1, imgID2, response2
    
    # creates a student record w/the minimum 5 attributes required
    # requires projUuid & projId
    def createImage04(self, project_id, user_id, token,projUuid, projId):
        
        # data to be used in post
        imgData = json.dumps({"images":[{"url":self.testUrl, 
                                         "name":self.testName, 
                                         "width":self.testWidth, 
                                         "height":self.testHeight, 
                                         "type":self.testType,
                                         "project_id":projUuid}]})
        
        # posts data and returns response
        response = self.postImage(project_id, user_id, 
                                  token, serviceUrl=self.serviceUrl, 
                                  data=imgData)
        
        # checks response
        imgID = self.responseCheck02(response, key="project_id", 
            expected=projId, 
            listInt=0, 
            code=201, 
            logMsg='new image created')
        
        # attempts to Get / Read the newly created Student Record
        response2 = self.serviceGet01(project_id, user_id, 
                                          token, serviceUrl=self.getUrl, 
                                          image_id = imgID)
        self.responseCheck03(response2, expected=self.testUrl, key="url", passMsg='new image retrieved from db')
        
                
        module_logger.info('new image created')
        self.added_imageIds.append(imgID)
        
        return imgID, response2
    
    
    # used in post tests that should yield a failure code 40x
    def responseCheck01(self, response, code, expected, passMsg, failMsg):
        if response.status_code == code:
            response_data = response.json()
            module_logger.debug(response_data)
            new_id, message = self.postResponseMessage(response, listInt = None, key = None)
            self.assertIsNone(new_id)
            self.assertEquals(message, expected)
            module_logger.info(passMsg)
        elif response.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response)
            self.fail('status code was 500')
        else:
            response_data = response.json()
            new_id, message = self.postResponseMessage(response, 0, "id")
            self.added_imageIds.append(new_id)
            module_logger.debug(response_data)
            module_logger.info(failMsg)
            module_logger.debug("status code was")
            module_logger.debug(response.status_code)
            self.fail(failMsg)
    
    # used in post tests that should yield a 200
    def responseCheck02(self, response, key, expected, listInt,code, logMsg):
        if response.status_code == code:
            response_data = response.json()
            module_logger.debug(response_data)
            new_id, message = self.postResponseMessage(response, listInt, key)
            self.added_imageIds.append(new_id)
            self.assertIsNotNone(new_id)
            self.assertEquals(message, expected)
            module_logger.info(logMsg)
            
            return new_id
        elif response.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response)
            self.fail('status code was 500')
        else:
            response_data = response.json()
            module_logger.debug(response_data)
            module_logger.info('FAIL : status code was not 200')
            module_logger.debug("status code was")
            module_logger.debug(response.status_code)
            self.fail('status code was not 200')
     
    # used to interrogate get response messages        
    def responseCheck03(self, response, expected, key, passMsg ):
        if response.status_code == 200:
            response_data = response.json()
            module_logger.info(response_data)
            new_id2, message2 = self.getResponseMessage(response, key)
            self.assertEquals(message2, expected)
            self.assertIsNotNone(new_id2)
            module_logger.debug(new_id2)
            module_logger.info(passMsg)
            return response_data
        elif response.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response)
            self.fail('status code was 500')
        else:
            response_data = response.json()
            module_logger.debug(response_data)
            module_logger.info('FAIL : status code was not 200. could not Get Image')
            module_logger.debug("status code was")
            module_logger.debug(response.status_code)
            self.fail('status code was not 200 could not Get Image')
     
    # used in negative get tests        
    def responseCheck04(self, response,code, expected, passMsg ):
        if response.status_code == code:
            response_data = response.json()
            module_logger.info(response_data)
            _, message2 = self.getResponseMessage(response)
            self.assertEquals(message2, expected)
            module_logger.info(passMsg)
            return response_data
        elif response.status_code == 500:
            module_logger.info('FAIL : status code was 500')
            module_logger.debug(response)
            self.fail('status code was 500')
        else:
            response_data = response.json()
            module_logger.debug(response_data)
            module_logger.info('FAIL : image was retreived')
            module_logger.debug("status code was")
            module_logger.debug(response.status_code)
            self.fail('FAIL : image was retreived')
            
    # headers used to connect to api    
    def basicHeaderInfo(self, project_id, user_id, token):
        header = dict()
        header['Content-Type'] = 'application/json'
        header['Accept'] = 'application/json'
        header['user_id'] = user_id
        header['project_id'] = project_id
        header['X-Subject-Token'] = token
        return header
    
   
    
    