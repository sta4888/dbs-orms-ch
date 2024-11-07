# dbs-orms-ch
CheatSheet)


```python
# SELECT * FROM myapp_userprofile WHERE user_id = (SELECT id FROM auth_user WHERE username = 'some_username');
User.objects.create_user(username='new_user', password='password')
```

```python
# INSERT INTO auth_user (username, password) VALUES ('new_user', 'password');
# SET @user_id = LAST_INSERT_ID();
user = User.objects.create_user(username='new_user', password='password')
```

