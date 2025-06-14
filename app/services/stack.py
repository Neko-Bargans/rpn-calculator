from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.stack import Stack


engine = create_engine("sqlite:////tmp/rpn.db")
session = Session(engine)


def list_operands() -> List[str]:
    return ["+", "-", "*", "/"]


def create_stack() -> Stack:
    new_stack = Stack()
    session.add(new_stack)
    session.commit()
    return new_stack


def list_stacks() -> List[Stack]:
    return session.query(Stack).all()


def get_stack_by_id(stack_id: int) -> Stack:
    if not isinstance(stack_id, int):
        raise HTTPException(status_code=400, detail="Stack id is not an int")

    stack = session.query(Stack).filter(Stack.id == stack_id).first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    return stack


def delete_stack_by_id(stack_id: int) -> None:
    if not isinstance(stack_id, int):
        raise HTTPException(status_code=400, detail="Stack id is not an int")

    stack = session.query(Stack).filter(Stack.id == stack_id).first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    session.query(Stack).filter(Stack.id == stack_id).delete()
    session.commit()


def add_value_to_stack_by_id(stack_id: int, value: int) -> Stack:
    if not isinstance(stack_id, int):
        raise HTTPException(status_code=400, detail="Stack id is not an int")
    if not isinstance(value, int):
        raise HTTPException(status_code=400, detail="value is not an int")

    stack = session.query(Stack).filter(Stack.id == stack_id).first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    stack.stack.append(value)
    session.query(Stack).filter(Stack.id == stack_id).update({"stack": stack.stack})
    session.commit()
    return stack


def apply_operand_on_a_stack_by_id(stack_id: int, operand: str) -> Stack:
    if not isinstance(stack_id, int):
        raise HTTPException(status_code=400, detail="Stack id is not an int")
    if not isinstance(operand, str):
        raise HTTPException(status_code=400, detail="Operand must be a str")

    stack = session.query(Stack).filter(Stack.id == stack_id).first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    if len(stack.stack) < 2:
        raise HTTPException(
            status_code=403, detail="Stack does not have at least two values"
        )
    match operand:
        case "+":
            stack.stack.append(stack.stack.pop() + stack.stack.pop())
        case "-":
            stack.stack.append(stack.stack.pop() - stack.stack.pop())
        case "*":
            stack.stack.append(stack.stack.pop() + stack.stack.pop())
        case "*":
            numerator = stack.stack.pop()
            denominator = stack.stack.pop()
            if denominator == 0:
                raise HTTPException(status_code=403, detail="Cannot divide by 0")
            stack.stack.append(numerator / denominator)
        case _:
            raise HTTPException(status_code=400, detail="Operand is not supported")
    session.query(Stack).filter(Stack.id == stack_id).update({"stack": stack.stack})
    session.commit()
    return stack
