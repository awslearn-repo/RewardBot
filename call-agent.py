import json
import boto3

# Initialize the Bedrock Agent Runtime client
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    # Extract user input prompt and session ID from the event
    try:
        user_prompt = event["prompt"]
        session_id = event["session_id"]
    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing required field: {str(e)}"})
        }

    # Invoke Bedrock Agent
    try:
        response = bedrock_agent_runtime.invoke_agent(
            agentId="A5UFARGCZ3",
            agentAliasId="WBU1YOH5ZW",
            sessionId=session_id,
            inputText=user_prompt
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Failed to invoke Bedrock Agent: {str(e)}"})
        }

    # Process Bedrock Agent response
    try:
        completion = ""
        traces = []

        for event in response.get("completion", []):
            try:
                trace = event["trace"]
                traces.append(trace['trace'])
            except KeyError:
                chunk = event["chunk"]
                completion += chunk["bytes"].decode()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "completion": completion,
                "traces": traces
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Failed to process Bedrock Agent response: {str(e)}"})
        }
