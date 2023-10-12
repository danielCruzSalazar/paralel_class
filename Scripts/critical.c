#include <omp.h>
#include <stdio.h>

double run_time, start_time = 0.0;
int glob = 0;
int sharedC = 0;
int main()
{
    start_time = omp_get_wtime();
#define THREAD 8
#define STEPS 1000000

#pragma omp parallel num_threads(omp_get_max_threads())
    {
        int counter = 0;
        int id = omp_get_thread_num();
        int threads_in = omp_get_num_threads();
        if (omp_get_thread_num() == 0)
        {
            glob = threads_in;
        }

        for (int i = id; i < STEPS; i += threads_in)
        {
            counter++;
        }
        printf("%d\n", counter);
#pragma omp critical
        {
            sharedC += counter;
        }
    }
    run_time = omp_get_wtime() - start_time;
    printf("threads:%d \ncontador final: %d\ntiempo: %lf\n", glob, sharedC, run_time);
}