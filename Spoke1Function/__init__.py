import logging

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = req.params.get('message')

    if not message:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            message = req_body.get('message')

    if message:

        ## Writes 'message' to the Service Bus Queue named 'msg'
        msg.set(message)

        return func.HttpResponse(f"Received {message}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a message in the query string or in the request body.",
             status_code=200
        )
