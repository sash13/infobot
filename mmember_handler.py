from matrix_bot_api.mhandler import MHandler


class MMemberHandler(MHandler):
  
    def __init__(self, handle_callback):
        MHandler.__init__(self, self.test_member, handle_callback)

    def test_member(self, room, event):
        if event['type'] == "m.room.member":
            return True
        return False