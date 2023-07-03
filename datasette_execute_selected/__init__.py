from datasette import hookimpl, Response
from datasette.utils import sqlite3
import json


@hookimpl
def extra_js_urls():
    return [
        "/-/static-plugins/datasette-execute-selected/datasette-execute-selected.js"
    ]


@hookimpl
def register_routes():
    return [
        (r"^/-/validate-query-selection$", validate_query_selection),
    ]


async def validate_query_selection(request, datasette):
    data = json.loads(await request.post_body())
    query = data.get("query")
    if not query:
        return Response.json({"error": "Missing query", "valid": False}, status=400)

    db = datasette.get_database()
    query = "explain {}".format(query)

    try:
        await db.execute(query, log_sql_errors=False)
        is_valid = True
    except Exception as ex:
        is_valid = False

    return Response.json({"valid": is_valid})
