import datetime
import json
import hashlib
class blockchain:
    def __init__(self) :
        #เก็บกลุ่มของ Block
        self.chain = [] #list ที่เก็บ block
        #genesis block ที่สมมุติขึ้นมา
        self.create_block(nonce = 1,previous_hash="0")
        self.create_block(nonce = 10,previous_hash="100")

    #Method สำหรับสร้าง block ขึ้นมาในระบบ blockchain
    def create_block(self,nonce,previous_hash):
        #เก็บส่วนประกอบของ block แต่ละ block
        block = {
            "index" : len(self.chain) + 1 , #index ของ block แรกมีค่าเป็น 1
            "timestamp": str(datetime.datetime.now()),
            "nonce":nonce,
            "previous_hash":previous_hash
        }
        self.chain.append(block) #นำ block ไปต่อกับ chain 
        return block
    
    #ให้บริการเกี่ยวกับ block ก่อนหน้า
    def get_previous_block(self):
        return self.chain[-1] #แสดงค่า block ก่อนหน้า
    #เข้ารหัส block
    def hash(self,block):
        #เรียงข้อมูลใน block แล้วแปลง python object (dict) = > json object
        encode_block = json.dumps(block,sort_keys=True).encode()
        #SHA-256
        return hashlib.sha256(encode_block).hexdigest()
    def proof_of_work(self,previous_nonce):
        #อยากได้ค่า Nonce ที่ส่งผลให้ได้ targerhash => 4 หลักแรก => 0000xxxxxxxxx
        new_nonce = 1 #ค่า nonce ที่ต้องการ
        check_proof = False #ตัวแปรที่เช็คค่า Nonce ให้ได้ตาม target ที่กำหนด
        
        #แก้โจทย์ทาง Math 
        while check_proof is False: #ตรวจสอบว่าที่อยู่ใน Check_proof เป็น False อยู่ (ยังหา Target hash ไม่ได้)
            #เลขฐาน 16 มา 1 ชุด 
            hashoperation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4] == "0000":
                check_proof = True
            else:
                new_nonce += 1
        return new_nonce
            
            
        
    
#ใช้งาน blockchain
blockchain = blockchain()
#เข้ารหัส block แรก
print(blockchain.hash(blockchain.chain[0]))
#เข้ารหัส block สอง
print(blockchain.hash(blockchain.chain[1]))
