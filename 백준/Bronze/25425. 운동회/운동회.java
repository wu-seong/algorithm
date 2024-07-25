import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer str = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(str.nextToken());
		int m = Integer.parseInt(str.nextToken());
		int a = Integer.parseInt(str.nextToken());
		int k = Integer.parseInt(str.nextToken());
		int max;
		if(n <= a) {
			max = n;
		}
		else {
			max = a;
		}
		int min;
		if((a-k)%m == 0) {
			min = ((a-k)/m)+1;
		}
		else {
			min = ((a-k)/m)+2;
		}
		if(a == k) {
			min = 1;
		}
		bw.write(String.valueOf(max)+" "+String.valueOf(min));
		bw.flush();
		bw.close();
	}
}
