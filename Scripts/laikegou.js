toast("��� ������ ������")    
 
if (text("ȥǩ��").exists()) {    
  toast("���ǩ��")      
  text("ȥǩ��").findOne().click();        
  sleep(4000);  
  }
    
if (text("��������").exists()) {   
  text("��������").findOne().click();        
  sleep(5000); 
  toast("ǩ�����")    
  back(); 
  sleep(2000);
  toast("ǩ���ɹ�")    }  
  
 while(text("��ȡ").exists()) {        
      text("��ȡ").findOne().click();        
      sleep(1600);        
      toast("��ȡ�ɹ�")    
 }    
  
 //2.��������
 while(textContains("ȥ���").exists()){
     //Ҫ֧�ֵĶ���
     toast("����ȥ���");
     textContains("ȥ���").findOne().click();
     sleep(7000);
     back();
     sleep(2000);
 }
  
 swipe(500,2000,500,1000,50);//�ϻ�
 sleep(2000);
   
  
 //2.��������  //��ʱ������������������޷���ɣ���ô�죿��
 while(textContains("ȥ��ע").exists()){
     toast("����ȥ��ע");
     textContains("ȥ��ע").findOne().click();
     sleep(7000);
  
     while(textContains("����ע").exists()){
         toast("���ڹ�ע");
         textContains("����ע").findOne().click();
         sleep(7000);
         back();
         sleep(3000);
     }
     back();
     sleep(3000);
     toast("��ע��ɿ�");
 }