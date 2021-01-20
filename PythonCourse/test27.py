# Python 2.7
import sys
import os
import datetime
import time

LOG_FOLDER = "C:\\Users\\davez_000\\PycharmProjects\\PythonCourse\\logs"

#-------------------------------------------------------------------------------------#
"""
    Remove any files in the specified folder that are older than the days_to_key
"""
def log_file_retention(log_folder,days_to_keep):

   print("Cleaning up files in %s that are greater than %d days old" % (log_folder,days_to_keep))

   # If the folder does not exist, the job will throw an exception

   # Build a list of the files in the log folder
   onlyfiles = [f for f in os.listdir(log_folder) if os.path.isfile(os.path.join(log_folder, f))]

   # Current time
   dt_ct = datetime.date.today()
   dt_ct_str = dt_ct.strftime("%Y-%m-%d")

   for f in onlyfiles:

      fp = "%s\\%s" % (log_folder,f)
      mtime = os.path.getmtime(fp)
      dt_mtime = datetime.date.fromtimestamp(mtime)
      dt_mtime_str = dt_mtime.strftime("%Y-%m-%d")

      dt_delta = dt_ct - dt_mtime

      if dt_delta.days > days_to_keep:
         os.remove(fp)
         print("Deleting file %s which was last modified on %s and is %d days old" % ( f, dt_mtime_str, dt_delta.days ) )

#-------------------------------------------------------------------------------------#
def main():

   print("Python program %s" % (sys.argv[0]))
   print("Python version %s" % (sys.version.split(" ")[0]))



#-------------------------------------------------------------------------------------#
"""
   Convential main function call 
"""
if __name__ == "__main__":
    main()
