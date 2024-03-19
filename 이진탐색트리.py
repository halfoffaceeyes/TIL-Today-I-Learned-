class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    # 처음 삽입 시
    if root is None:
        return TreeNode(key)
    else:
        # 작다면 왼쪽부터 삽입 시도
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root



def search(root, key):
    # root 를 찾는다면
    if root is None or root.value == key:
        return root
    
    # key 값이 더 크다면 왼쪽부터 탐색
    if root.value > key:
        return search(root.left, key)
    
    # 크다면 오른쪽 탐색
    return search(root.right, key)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


def find_max_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # 삭제하려는 노드가 리프 노드이거나 하나의 자식만 가지는 경우
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # 삭제하려는 노드가 두 개의 자식을 가지는 경우
        # 1. 왼쪽 서브 트리의 가장 큰 값
        temp = find_max_node(root.left)
        root.value = temp.value
        root.left = delete_node(root.left, temp.value)
        # 2. 오른쪽 서브 트리의 가장 작은 값
        # temp = find_min_node(root.right)
        # root.value = temp.value
        # root.right = delete_node(root.right, temp.value)
        # 두 가지가 가능한 후보

    return root


# 이진 탐색 트리 생성 및 사용 예제
# arr = [8, 3, 10, 2, 5, 14, 11, 16]
arr = [9, 4, 12, 3, 6, 15, 13, 17]
root = insert(None, arr[0])
for el in arr[1:]:
    insert(root, el)
    # 중간 디버깅용 출력코드
    # inorder_traversal(root)
    # print()

# 특정 값 검색 예제
key_to_search = 10
result = search(root, key_to_search)
if result:
    print(f"{key_to_search}를 찾았습니다.")
else:
    print(f"{key_to_search}를 찾을 수 없습니다.")

# 노드 삭제 예제
key_to_delete = 13
inorder_traversal(root)
print()
root = delete_node(root, key_to_delete)
inorder_traversal(root)
print()

root = delete_node(root, 12)
inorder_traversal(root)
print()

root = delete_node(root, 9)
inorder_traversal(root)
print()

print(root.value)
