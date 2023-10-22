#include <stdio.h>
#include <omp.h>

#define Threads 1

static long num_steps = 1000000000;
double step = 0.0;
double pi = 0.0;
double start_time, run_time;
double sum=0.0;
int main()
{
	step = 1.0 / (double)num_steps;
	start_time = omp_get_wtime();
	omp_set_dynamic(0);
	omp_set_num_threads(Threads);
#pragma omp parallel for reduction(+:sum)
		for (int i = 0; i < num_steps; i ++){
			double x = (i - 0.5) * step;
			sum += 4.0 / (1.0 + x * x);
		}
	printf("\nsum : %ld", sum);
	pi = step * sum;
	run_time = omp_get_wtime() - start_time;
	printf("\n pi with %ld steps is %lf in %lf seconds with %d threads", num_steps, pi, run_time, Threads);
}