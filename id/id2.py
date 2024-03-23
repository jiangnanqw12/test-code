import uuid
short_uuid = str(uuid.uuid4())[:8]  # 截取前8位
print(f"{short_uuid}")
