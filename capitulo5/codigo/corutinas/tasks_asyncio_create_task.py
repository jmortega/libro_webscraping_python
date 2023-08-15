import asyncio
import time
 
async def my_task(seconds):
    """
   Una tarea que dure los segundos pasados por parámetro
    """
    print('Esta tarea le llevara {} segundos en completarse'.format(seconds))
    time.sleep(seconds)
    return 'task finished'
  
if __name__ == '__main__':
    my_event_loop = asyncio.get_event_loop()
    try:
        print('comienzo la creación de tareas')
        task_obj = my_event_loop.create_task(my_task(seconds=2))
        task_obj = my_event_loop.create_task(my_task(seconds=5))
        my_event_loop.run_until_complete(task_obj)
    finally:
        my_event_loop.close()
 
    print("El resultado de la tarea es: {}".format(task_obj.result()))

