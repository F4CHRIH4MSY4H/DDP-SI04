{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPZsQb4nrKay0jLDhRz/9qo"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":10,"metadata":{"id":"eTDitHNIi2Aq","executionInfo":{"status":"ok","timestamp":1730361613137,"user_tz":-420,"elapsed":997,"user":{"displayName":"fachri hmsyh","userId":"11081833338248604291"}}},"outputs":[],"source":["\n","numbers = [\n","    # ... daftar bilangan yang sudah diberikan ...\n","]\n","\n","i = 0\n","while i < len(numbers):\n","    if numbers[i] % 2 != 0:  # Cek apakah bilangan ganjil\n","        print(numbers[i])\n","    if numbers[i] > 553:  # Hentikan jika sudah melewati 553\n","        break\n","    i += 1"]}]}