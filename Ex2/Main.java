import java.util.*;

public class Main{
  public static void main(String[]args){
    new Main().run();
  }
  private void run(){
    Scanner sc = new Scanner(System.in);
    int Heap_size = sc.nextInt();
    int[] A =new int[Heap_size+1];
    for (int i=1; i<=Heap_size; i++) {
        A[i] = sc.nextInt();
    }
    Heap_bottom_up(A,Heap_size);

    for(int i=1;i<=Heap_size;i++)
      System.out.print(A[i]+" ");
      System.out.println();
  }

  void Heap_bottom_up(int[] A,int Heap_size){
    for (int i = Heap_size/2; i >= 1; i--){
      max_Heappify(A,i);
    }
  }

  private void max_Heappify(int[] A,int i){
    int l = i*2;
    int r = i*2+1;
    int H = A.length-1;
    int largest=-1;
    if(l<= H && A[l] > A[i])
      largest = l;
    else
      largest = i;
    if(r<= H && A[r] > A[largest])
      largest = r;
      if(largest != i){
      exchange(A,i,largest);
      max_Heappify(A,largest);
      }
  }

  private void exchange(int[] A,int i,int largest){
    int temp = A[i];
    A[i] = A[largest];
    A[largest] = temp;
  }
}
