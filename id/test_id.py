import uuid


def create_custom_uuid(timestamp, category):
    # 将时间戳和分类标识转换为字符串并拼接
    base_str = f"{category}_{timestamp}"
    # 生成一个随机的UUID
    random_uuid = uuid.uuid4().hex
    # 将自定义的部分与随机UUID拼接
    custom_uuid = base_str + "_" + \
        random_uuid[:len(random_uuid) - len(base_str)]
    return custom_uuid


def test_uuid():
    # 示例
    custom_uuid = create_custom_uuid(1710564935, "01")
    print(custom_uuid)


def main():
    timestamp_uuid = uuid.uuid1()
    print(f"{timestamp_uuid}")


if __name__ == "__main__":
    main()
