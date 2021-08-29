# -*- coding: utf-8 -*-
import json
import os

from aws_lambda_powertools import Logger, Tracer
from chalice import Chalice, ConvertToMiddleware, Cron

from chalicelib import Database

app = Chalice(app_name="bobotinho", debug=os.environ.get("DEBUG"))

logger = Logger(service=app.app_name)
tracer = Tracer(service=app.app_name)
app.register_middleware(ConvertToMiddleware(logger.inject_lambda_context))
app.register_middleware(ConvertToMiddleware(tracer.capture_lambda_handler))

db: Database = Database(
    name=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
)


def reset_users_daily(db: Database) -> None:
    """Reset users daily cookies (update 'daily' to 1).

    Args:
        db (Database): database instance
    """
    db.execute("UPDATE public.cookie SET daily = 1 WHERE daily = 0")


def reset_sponsors_daily(db: Database) -> None:
    """Reset sponsors daily cookies (update 'daily' to 2 if 'sponsor' is True).

    Args:
        db (Database): database instance
    """
    ids = db.fetch("SELECT id FROM public.user WHERE sponsor IS TRUE;")
    if ids:
        ids = tuple(map(lambda x: x[0], ids))  # [(1,), (2,), ...] -> [1, 2, ...]
        db.execute(f"UPDATE public.cookie SET daily = 2 WHERE id IN {ids}")


@app.schedule(expression=Cron("0", "9", "*", "*", "?", "*"), name="reset-daily")
def reset_daily(event: dict, context: object = None) -> bool:
    """Connect to database and reset daily cookies when Lambda function is invoked.

    Args:
        event (dict): information from the invoke
        context (object, optional): information about the invocation, function
                                    and execution env. Defaults to None.

    Returns:
        bool: indicates success or failure
    """
    try:
        logger.info("Initiating...")
        db.init()
        reset_users_daily(db)
        reset_sponsors_daily(db)
        return {"StatusCode": 200, "body": json.dumps({"FunctionError": "Unhandled"})}
    except Exception as e:
        logger.exception(e)
        return {"StatusCode": 500, "body": json.dumps({"FunctionError": str(e)})}
    finally:
        logger.info("Closing...")
        db.close()
