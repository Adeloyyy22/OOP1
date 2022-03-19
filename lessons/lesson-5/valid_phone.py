"""re - Regular Expenssion"""
import re

phone = "+996-707-77-77-77"
result = re.match(r"^\+([0-9]{1,3})-([0-9]{1,3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)

try:
    if phone[result.start():result.end()] == phone:
        print("Phone Number Valid!")
    else:
        raise "Is not valid phone