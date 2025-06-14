from fastapi import FastAPI
import app.services.stack as stack_services

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/rpn/op")
def list_operands():
    return {"operands": stack_services.list_operands()}


@app.post("/rpn/op/{op}/stack/{stack_id}", status_code=201)
def apply_operands(op: str, stack_id: int):
    return stack_services.apply_operand_on_a_stack_by_id(stack_id, op).to_json()


@app.post("/rpn/stack", status_code=201)
def create_stack():
    return stack_services.create_stack().to_json()


@app.get("/rpn/stack")
def list_stack():
    return {"stacks": stack_services.list_stacks()}


@app.delete("/rpn/stack/{stack_id}", status_code=204)
def delete_stack(stack_id: int):
    stack_services.delete_stack_by_id(stack_id)


@app.post("/rpn/stack/{stack_id}", status_code=201)
def add_value(stack_id: int, value: int):
    return stack_services.add_value_to_stack_by_id(stack_id, value).to_json()


@app.get("/rpn/stack/{stack_id}")
def get_stack(stack_id: int):
    return stack_services.get_stack_by_id(stack_id).to_json()
