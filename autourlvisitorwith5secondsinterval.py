count = 0
while True:
    print(count)
    import webbrowser
    import time
    new=2;
    url="http://google.com";
    webbrowser.open(url,new=new);
    count += 1
    time.sleep(5)
    if count >=5000:
        break
