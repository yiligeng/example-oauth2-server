### 1. Install requirements

```bash
pip install -r requirements.txt
```

### 2. Disable check https (DO NOT SET THIS IN PRODUCTION)

```bash
export AUTHLIB_INSECURE_TRANSPORT=1
```

### 3. Flask run

```bash
python -m flask run
```

### 4. Login in Oauth2 Server

##### 		4.1 Create a client

```
http://127.0.0.1:5000/
```

##### 			Client Detail

```
Client Info
  client_id: NpuAvsQb7T6T0lu8NkpxeBfw
  client_secret: 9xqJpUwD9EoaOiiYC3zTejBsvxrg0gljJ213GZZLGroUOmZ0
  client_id_issued_at: 1622082000
  client_secret_expires_at: 0
Client Metadata
  client_name: test
  client_uri: https://authlib.org/
  grant_types: ['authorization_code', 'password']
  redirect_uris: ['https://authlib.org/']
  response_types: ['code']
  scope: profile
  token_endpoint_auth_method: client_secret_basic
```

### 5. <font color=bluepink>Resource Owner Password Credentials Grant</font> [( one of four patterns )](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)

##### 	5.1 Allow App get user's usename and password

###### 		5.1.1 Send cliend_id, clilent_secret, usename, password

```bash
curl -u ${client_id}:${client_secret} -XPOST http://127.0.0.1:5000/oauth/token -F grant_type=password -F username=${username} -F password=valid -F scope=profile
```

###### 		5.1.2 Response

```
{"access_token": "LTX7SuoHS0SnsRlYKLHRkAv1pJ7qvJk883C6l4f771", "expires_in": 864000, "refresh_token": "nNPcEZ4YzrAboJEnUTZTwTJb6IdjYACXmGOvgpPnQZRRMPpB", "scope": "profile", "token_type": "Bearer"}%
```

##### 	5.2  Test access_token

###### 			5.2.1 Use access_token 

```bash
curl -H "Authorization: Bearer ${access_token}" http://127.0.0.1:5000/api/me
```

###### 		5.2.2 Response

```
{
  "id": 3,
  "username": "gyl"
}
```

### 6. <font color=bluepink>Authorization code flow example</font> [( one of four patterns )](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)

##### 	6.1 Test authorization code flow

###### 		6.1.1 Open URL in browser 

​			Response_type, client_id, scope			 

```
open http://127.0.0.1:5000/oauth/authorize?response_type=code&client_id=${client_id}&scope=profile
```

###### 		6.1.2 Login in and oauth the APP

​			After granting the authorization,  be redirected to `${redirect_uri}/?code=${code}`

```
https://authlib.org/?code=tAwtD4OKj79OBa97qxTTLdntyRXTpFKhVmzm30apJSPD8YFQ
```

###### 		6.1.3 APP Send code to authorization to get access token

```
curl -u ${client_id}:${client_secret} -XPOST http://127.0.0.1:5000/oauth/token -F grant_type=authorization_code -F scope=profile -F code=${code}
```

​			Response

```
{"access_token": "9pieJnG7eALU8pKJ6xO7VMzbRGT2qkdYU7QOPib1kb", "expires_in": 864000, "scope": "profile", "token_type": "Bearer"}
```

###### 		6.1.4 Test access_token

```
curl -H "Authorization: Bearer ${access_token}" http://127.0.0.1:5000/api/me
```

​			Response

```
{"id": 3,"username": "gyl"}
```





