toast("请打开 宠汪汪 任务栏")    
 
if (text("去签到").exists()) {    
  toast("点击签到")      
  text("去签到").findOne().click();        
  sleep(4000);  
  }
    
if (text("立即翻牌").exists()) {   
  text("立即翻牌").findOne().click();        
  sleep(5000); 
  toast("签到完毕")    
  back(); 
  sleep(2000);
  toast("签到成功")    }  
  
 while(text("领取").exists()) {        
      text("领取").findOne().click();        
      sleep(1600);        
      toast("领取成功")    
 }    
  
 //2.浏览任务①
 while(textContains("去逛逛").exists()){
     //要支持的动作
     toast("存在去逛逛");
     textContains("去逛逛").findOne().click();
     sleep(7000);
     back();
     sleep(2000);
 }
  
 swipe(500,2000,500,1000,50);//上滑
 sleep(2000);
   
  
 //2.浏览任务②  //有时候浏览过，但是任务无法完成？怎么办？？
 while(textContains("去关注").exists()){
     toast("存在去关注");
     textContains("去关注").findOne().click();
     sleep(7000);
  
     while(textContains("并关注").exists()){
         toast("存在关注");
         textContains("并关注").findOne().click();
         sleep(7000);
         back();
         sleep(3000);
     }
     back();
     sleep(3000);
     toast("关注完成咯");
 }