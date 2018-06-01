import java.util.Scanner;

public class mergesort {
    public static void main(String[] args) {
        new mergesort().run();
    }
    
    private void run() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        mergeSort(A, 0, n);
        System.out.print(A[0]);
        for (int i = 1; i < n; i++) {
            System.out.print(" " +A[i]);
        }
        System.out.println();
    }
    private void merge(int[] A, int left, int mid, int right) {
        int n1 = mid - left;
        int n2 = right - mid;
        int[] l = new int[n1 + 1];
        int[] r = new int[n2 + 1];
        for (int i = 0; i < n1; i++)
            l[i] = A[left + i];
        for (int i = 0; i < n2; i++)
            r[i] = A[mid + i];
        l[n1] = Integer.MAX_VALUE;
        r[n2] = Integer.MAX_VALUE;
        int L = 0;
        int R = 0;
        for (int k = left; k < right; k++) {
            if (l[L] <= r[R]) {
                A[k] = l[L++];
            } else {
                A[k] = r[R++];
            }
        }
    }
    
    private void mergeSort(int[] num, int left, int right) {
        if (left + 1 < right) {
            int mid = (left + right) / 2;
            mergeSort(num, left, mid);
            mergeSort(num, mid, right);
            merge(num, left, mid, right);
        }
    }
    
    
}
