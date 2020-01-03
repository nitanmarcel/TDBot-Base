from .telegram import EventHandler, on_event, td_api
from .telegram.AuthorisationHandler import log_in


@on_event(td_api.updateNewMessage)
def test(event: td_api.updateNewMessage):
    print(event.message.stringify())


if __name__ == '__main__':
    log_in(session_name='tdbot', api_hash='a123456789abcdf', api_id=12345, bot_token='12345:ABCDFGH_abc-2abABCDF1')
    EventHandler.listenToEvents()
