def cnt_sum_triple(a, n):
    cnt = 0
    a.sort()  # Sắp xếp mảng để sử dụng phương pháp hai con trỏ
    for i in range(n - 2):
        if i > 0 and a[i] == a[i - 1]:
            continue  # Bỏ qua các phần tử trùng lặp
        left = i + 1
        right = n - 1
        while left < right:
            total = a[i] + a[left] + a[right]
            if total == 0:
                cnt += 1
                # Bỏ qua các phần tử trùng lặp ở bên trái
                while left < right and a[left] == a[left + 1]:
                    left += 1
                # Bỏ qua các phần tử trùng lặp ở bên phải
                while left < right and a[right] == a[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Tăng con trỏ trái nếu tổng nhỏ hơn 0
            else:
                right -= 1  # Giảm con trỏ phải nếu tổng lớn hơn 0
    return cnt

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])  # Đọc số lượng test cases
    idx += 1
    for _ in range(t):
        n = int(data[idx])  # Đọc số lượng phần tử của mảng
        idx += 1
        a = list(map(int, data[idx:idx + n]))  # Đọc mảng
        idx += n
        print(cnt_sum_triple(a, n))  # In kết quả

if __name__ == "__main__":
    main()