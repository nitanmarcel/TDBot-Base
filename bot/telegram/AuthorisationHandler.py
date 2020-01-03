from . import td_api, td_recieve, td_send


def log_in(session_name, api_hash, api_id, bot_token):
    while True:
        event = td_recieve()
        if event:
            if isinstance(event, td_api.updateAuthorizationState):
                auth_state = event.authorization_state
                if isinstance(auth_state, td_api.authorizationStateWaitTdlibParameters):
                    r = td_send(
                        td_api.setTdlibParameters(parameters={
                                                       'database_directory': str(session_name),
                                                       'use_message_database': True,
                                                       'use_secret_chats': True,
                                                       'api_id': int(api_id),
                                                       'api_hash': str(api_hash),
                                                       'system_language_code': 'en',
                                                       'device_model': 'Desktop',
                                                       'system_version': 'Linux',
                                                       'application_version': '1.0',
                                                       'enable_storage_optimizer': True}
                        ))

                if isinstance(auth_state, td_api.authorizationStateWaitEncryptionKey):
                    td_send(
                        td_api.checkDatabaseEncryptionKey(key='1234gtst'))

                if isinstance(auth_state, td_api.authorizationStateWaitPhoneNumber):
                    td_send({'@type': 'checkAuthenticationBotToken',
                             'token': bot_token})
                if isinstance(auth_state, td_api.authorizationStateReady):
                    print('Authorized!')
                    return
