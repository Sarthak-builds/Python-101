from fastmcp import FastMCP


mcp = FastMCP("calculator-server")


@mcp.tool
async def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """Perform a basic arithmetic operation on two numbers.

    Supported operations: add, subtract, multiply, divide.
    """
    import asyncio

    await asyncio.sleep(0)  # yield control, async-safe point

    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "subtract":
            result = first_num - second_num
        elif operation == "multiply":
            result = first_num * second_num
        elif operation == "divide":
            result = first_num / second_num
        else:
            return {
                "error": f"Unsupported operation: {operation}. "
                "Supported operations are add, subtract, multiply, divide."
            }
        return {
            "first_num": first_num,
            "second_num": second_num,
            "operation": operation,
            "result": result,
        }
    except ZeroDivisionError:
        return {"error": "Division by zero is not allowed."}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
