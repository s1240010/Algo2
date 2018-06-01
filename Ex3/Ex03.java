import java.util.*;


public class Ex03{

  int n,time;
  int[] f_time;
  int[] d_time;
  int[] Color;
  boolean[][] M;
 public static void main(String[] args) {
    new Ex03().run();
  }

  private void run(){
    int u,v,k;
    Scanner sc =new Scanner(System.in);
    n = sc.nextInt();
    M = new boolean[n][n];
    Color = new int[n];
    f_time = new int[n];
    d_time = new int[n];
    for (int i=0;i<n ;i++ ) {
      u = sc.nextInt();
      v = sc.nextInt();
      u--;
      for (int j=0;j<v;j++) {
          k = sc.nextInt();
          M[u][k-1] = true;
      }
    }
    dfs();
  }

  private  void dfs(){
    for(int i=0;i<n;i++){
      if(Color[i]==0)
        dfs_vist(i);
    }
    for(int i=0;i<n;i++)
      System.out.println("Node "+(i+1)+" Discovering time is "+d_time[i]+"  finishing time is "+f_time[i]);
  }

  private void dfs_vist(int u){
    Color[u] = 1;
    d_time[u] = ++time;
    for(int i=0;i<n;i++){
      if(M[u][i]==false) continue;
      if(Color[i]==0){
        dfs_vist(i);
      }
    }
    Color[u] = 2;
    f_time[u]=++time;
  }
}
