import redis
import config as con
import functions as func

redis_con = redis.Redis(host=con.HOST, port=con.PORT, db=con.DB)


def cache_message(chat_id, message):
    message_key = f"{chat_id}: {message}"

    if redis_con.get(message_key):
        func.send_notification_dupl(chat_id)
        return True

    redis_con.set(message_key, 'Хз', ex=30)
    return False
