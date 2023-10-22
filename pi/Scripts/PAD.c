#include <stdio.h>
#include <omp.h>

#define PAD 8
#define Threads 8

static long num_steps = 1000000000;
double step = 0.0;
double pi = 0.0;
double start_time, run_time;
int glob_threads = 0;
double arr[Threads][PAD];
int main()
{
	step = 1.0 / (double)num_steps;
	start_time = omp_get_wtime();
	omp_set_dynamic(0);
	omp_set_num_threads(Threads);
#pragma omp parallel
	{
		int id = omp_get_thread_num();
		int threads_in = omp_get_num_threads();

		if (id == 0)
		{
			glob_threads = threads_in;
		}
		for (int i = id; i < num_steps; i += threads_in)
		{
			double x = (i - 0.5) * step;
			arr[id][0] += 4.0 / (1.0 + x * x);
		}
	}

	double sum = 0.0;
	for (int i = 0; i < 32; i++)
	{
		sum += arr[i][0];
	}
	printf("\nsum : %ld", sum);
	pi = step * sum;
	run_time = omp_get_wtime() - start_time;
	printf("\n pi with %ld steps is %lf in %lf seconds with %d threads and %d PAD\n", num_steps, pi, run_time, glob_threads, PAD);
}