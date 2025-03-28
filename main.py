from flask import Flask, render_template , request ,redirect ,url_for
from connection import connection_databases,Execute_data,Execute_data_insert
import requests

app = Flask(__name__, template_folder="template")
    
@app.route("/home",methods=['get','post'])
def home():

    
    url = "https://notify-api.line.me/api/notify"
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Authorization' : "Bearer 7lVpHVzPrquKZ3M4aucCt7SBuXj5tMfw8oWuQSqQTWx"
                }

    # ประกาศให้เป็น str
    order_text = ""
    stock_text = ""
    stockgrp_text = ""
    stockgrp_code = None
    customer_text = ""
    customergrp_text = ""
    customergrp_code = ""
    select_value = None
    select_stock = None
    select_edit = None


    button_search = request.form.get("button_serch")
    button_add = request.form.get("button_add")
    button_edit = request.form.get("button_edit")
    button_delete = request.form.get("button_delete")
    button_selectedit = request.form.get("button_selectedit")


    result = connection_databases()
    
    
    if result > 0:

        query = "SELECT * FROM tbCustomer"
        result_customer = Execute_data(query)
        customer_text = result_customer

        query = "SELECT * FROM tbStock"
        result_stock = Execute_data(query)
        stock_text = result_stock

        query = "SELECT * FROM tbCustomerGrp"
        result_customergrp = Execute_data(query)
        customergrp_text = result_customergrp

        query = "select * from tb_Order"
        result_order = Execute_data(query)
        order_text = result_order

        query = "SELECT * FROM tbStockGrp"
        result_stockgrp = Execute_data(query)
        stockgrp_text = result_stockgrp

        if 'button_search' in request.form:
            select_value = request.form.get('customer')
            print("ค้นหา",button_search)

            if select_value is not None:
                print("select_value if")

                for row in customer_text:
                    print( "for in  row" ,row[0])
                    if row[0] == select_value:
                        row[1]
                        print("row 1 ",row[1])
                        customergrpcode = row[1]

                        query = "SELECT CustGrpName FROM tbCustomerGrp WHERE CustGrpCode = " + customergrpcode
                        result_customergrpcode = Execute_data(query)
                        for row in result_customergrpcode:
                            customergrp_text = row[0]
                            break
                        break
                    
                    else:
                        print("else")
            
        elif 'button_add' in request.form:
            button_add = request.form.get("button_add") 
            print ("เพิ่ม", button_add)

            select_value = request.form.get('customer')
            select_stock = request.form.get ('stock')
            print("name",select_value)
            print("stcok",select_stock)

            customer_result = Execute_data(f"select *from tbCustomer where CustCode = '{select_value}'")
            if customer_result:
                 customer_numname = customer_result[0][2]
                 customer_na = customer_result[0][3]
                 customer_tell = customer_result[0][5]
                 customergrp_code = customer_result[0][1]

            customergrp_result = Execute_data(f"select *from tbCustomerGrp where CustGrpCode = '{customergrp_code}'")
            if customergrp_result:
                 customer_namegrp = customergrp_result[0][1]

            for row in stock_text:
                 if select_stock == row[0]:
                    stockgrp_code = row[1]
                    print(stockgrp_code)
                    stock_result = Execute_data(f"select *from tbStock where StockCode = '{select_stock}'")
                    if stock_result:
                         Stock_name = stock_result[0][4]
                    query = f"INSERT INTO tb_Order (CustCode ,StockCode, StockGrpCode,states) VALUES ('{select_value}','{select_stock}','{stockgrp_code}','1')"
                    print("insert :",Execute_data_insert(query))

                    if Stock_name == "แป้งมันสำปะหลัง":
                        imag_url = "https://inwfile.com/s-cm/07qaf1.jpg" #1
                    elif Stock_name == "แป้งข้าวจ้าว":
                        imag_url = "https://inwfile.com/s-cm/edb25s.jpg" #2
                    elif Stock_name == "แป้งอเนกประสงค์":
                        imag_url = "https://inwfile.com/s-cm/sdsvse.jpg" #3
                    elif Stock_name == "แป้งสาลี":
                        imag_url = "https://image.makewebcdn.com/makeweb/m_1920x0/LnLGuwlBA/DefaultData/%E0%B9%81%E0%B8%9B%E0%B9%89%E0%B8%87%E0%B9%80%E0%B8%8A%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A3%E0%B8%B5%E0%B9%88%E0%B8%9F%E0%B9%89%E0%B8%B2_1_%E0%B8%81%E0%B8%B4%E0%B9%82%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B1%E0%B8%A1.jpg" #4
                    elif Stock_name == "แป้งลิสง":
                        imag_url = "https://www.bulksupplements.com/cdn/shop/files/Peanut-Flour-Protein-Powder-1kg_f095e8ba-0284-4cca-aaa7-36dd0fe69ada.jpg?v=1698082069" #5
                    elif Stock_name == "นมข้นหวาน":
                        imag_url = "https://inwfile.com/s-fi/9suz3v.jpg" #6
                    elif Stock_name == "นมข้นจืด":
                        imag_url = "https://inwfile.com/s-cm/0k0hp0.jpg" #7
                    elif Stock_name == "นมโอ๊ต":
                        imag_url = "https://oatside.com/wp-content/uploads/2021/09/OAT_Pkg_Web_Barista.jpg" #8
                    elif Stock_name == "นมสด":
                        imag_url = "https://cdn8.devgodigit.net/wp-content/uploads/2021/09/30183501/001844466_P.jpg" #9
                    elif Stock_name == "วานิลา":
                        imag_url = "https://sordaotieam.com/cdn/shop/products/sd00091.jpg?v=1624442197" #10
                    elif Stock_name == "บลูฮาวาย":
                        imag_url = "https://m.media-amazon.com/images/I/61kBXnxgC8L._AC_UF1000,1000_QL80_.jpg" #11
                    elif Stock_name == "สตอเบอรรี่":
                        imag_url = "https://www.1883.com/app/uploads/2021/05/sirop_fraise-1883_ps-1.jpg" #12
                    elif Stock_name == "คาราเมล":
                        imag_url = "https://www.caffacoffeemaker.com/wp-content/uploads/2023/12/%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2-108-scaled.jpg" #13
                    elif Stock_name == "กุหลาบ":
                        imag_url = "https://www.1883.com/app/uploads/2021/05/sirop_rose-1883_ps.jpg" #14
                    elif Stock_name == "มะพร้าว	":
                        imag_url = "https://www.1883.com/app/uploads/2021/05/sirop_noix-de-coco-1883_ps.jpg" #15
                    elif Stock_name == "แอปเปิ้ลเขียว":
                        imag_url = "https://www.1883.com/app/uploads/2021/05/sirop_pomme-verte-1883_ps.jpg" #16
                    elif Stock_name == "ลิ้นจี้":
                        imag_url = "https://www.1883.com/app/uploads/2021/05/sirop_litchi-1883_ps.jpg" #17

                    message_text = {
                    f">> รายการการสั่งซื้อสินค้า ร้าน BakeCraft Supplies <<\n\n"
                    f"🛒 ข้อมูลการสั่งซื้อสินค้า\n"
                    f"👤 ชื่อลูกค้า: {customer_numname} {customer_na}\n"
                    f"📞 เบอร์ลูกค้า: {customer_tell}\n"
                    f"🏷️ ประเภทลูกค้า: {customer_namegrp}\n"
                    f"📦 สินค้า: {Stock_name}\n"
                }
                    if imag_url :
                        message = {
                            "message": message_text,
                            "imageThumbnail" : imag_url,
                            "imageFullsize" : imag_url
                        }
                    else :
                         message = {"message": message_text}
            
            res = requests.post(url=url, headers=headers, data=message)

            select_value = None
            select_stock = None

            return redirect(url_for("home"))
            
        elif 'button_selectedit' in request.form:
            select_edit = request.form.get("button_selectedit")
            print ("แก้ไข", button_selectedit)

            query = 'select * from tb_Order where SoCode = ' + select_edit
            result_select = Execute_data(query)
            select_text = result_select
            for row in select_text :
                select_value = row[1]
                select_stock = row[2]
                break

            for row in customer_text: # ประกาศ row ใน customer_text และให้ลูปวนตามข้อมูลที่มี
                print( "for in  row" ,row[0])
                if row[0] == select_value: # เปรียบเทียบว่าตัว select_value มันเท่ากับ ข้อมูลอันที่ 0 ของแถวแต่ละแถวในcustomer_text
                    row[1]
                    print("row 1 ",row[1])
                    customergrpcode = row[1]

            query = "SELECT CustGrpName FROM tbCustomerGrp WHERE CustGrpCode = " + customergrpcode
            result_customergrpcode = Execute_data(query)
            for row in result_customergrpcode:
                customergrp_text = row[0]
                break


        elif 'button_edit' in request.form:
                
                print ("แก้ไข",button_edit)
                button_edit = request.form.get("button_edit")  # รับค่าปุ่มแก้ไข
                customer_name = request.form.get("customer")  # รับค่าชื่อจากดรอปดาวน์
                product_name = request.form.get("stock")  # รับค่าสินค้าจากดรอปดาวน์

                olddata = Execute_data(f"select CustCode,StockCode from tb_Order where SoCode = '{button_edit}'")
                if olddata:
                    oldCustCode,oldStockCode = olddata[0]
                    customer_result = Execute_data(f"select *from tbCustomer where CustCode = '{oldCustCode}'")
                    if customer_result:
                        customer_old_numname = customer_result[0][2]
                        customer_old_na = customer_result[0][3]
                        customer_old_tell = customer_result[0][5]
                        customergrp_old_code = customer_result[0][1]

                        customergrp_result = Execute_data(f"select *from tbCustomerGrp where CustGrpCode = '{customergrp_old_code}'")
                    if customergrp_result:
                        customer_old_namegrp = customergrp_result[0][1]
                    Stock_result = Execute_data(f"select *from tbStock where StockCode = '{oldStockCode}'")
                    if Stock_result:
                         Stock_old = Stock_result[0][4]

                

                print("แก้ไข SoCode:", button_edit)
                print("อัปเดตชื่อลูกค้าเป็น:", customer_name)
                print("อัปเดตสินค้าเป็น:", product_name)

                for row in stock_text: # ประกาศ row ใน customer_text และให้ลูปวนตามข้อมูลที่มี
                    if row[0] == product_name: # เปรียบเทียบว่าตัว select_value มันเท่ากับ ข้อมูลอันที่ 0 ของแถวแต่ละแถวในcustomer_text
                        row[1]
                        stockgrp_code = row[1]
                        print("row 1 ", row[1])
    


                query = f"update tb_Order set CustCode = '{customer_name}',StockCode = '{product_name}',StockGrpCode = '{stockgrp_code}' where SoCode = '{button_edit}'"
                print("insert :",Execute_data_insert(query))
                print("อัปเดตข้อมูลสำเร็จ")
                
                customer_result = Execute_data(f"select *from tbCustomer where CustCode = '{customer_name}'")
                if customer_result:
                    customer_numname = customer_result[0][2]
                    customer_na = customer_result[0][3]
                    customer_tell = customer_result[0][5]
                    customergrp_code = customer_result[0][1]

                customergrp_result = Execute_data(f"select *from tbCustomerGrp where CustGrpCode = '{customergrp_code}'")
                if customergrp_result:
                    customer_namegrp = customergrp_result[0][1]
                stock_result = Execute_data(f"select *from tbStock where StockCode = '{product_name}'")
                if stock_result:
                    Stock_name = stock_result[0][4]

                message_text = {
                f">> รายการการสั่งซื้อสินค้า ร้าน BakeCraft Supplies <<\n\n"
                f"⚠️ มีการแก้ไขข้อมูล\n\n"
                f"🛒 ข้อมูลการสั่งซื้อสินค้าของลูกค้าเก่า\n"
                f"👤 ชื่อลูกค้า: {customer_old_numname} {customer_old_na}\n"
                f"📞 เบอร์ลูกค้า: {customer_old_tell}\n"
                f"🏷️ ประเภทลูกค้า: {customer_old_namegrp}\n"
                f"📦 สินค้า: {Stock_old}\n"
                f"-----------------------------------\n"
                f"🛒 ข้อมูลการสั่งซื้อสินค้าของลูกค้าใหม่\n"
                f"👤 ชื่อลูกค้า: {customer_numname} {customer_na}\n"
                f"📞 เบอร์ลูกค้า: {customer_tell}\n"
                f"🏷️ ประเภทลูกค้า: {customer_namegrp}\n"
                f"📦 สินค้า: {Stock_name}\n"
                 }
                
                message = {"message": message_text}
                
                res = requests.post(url=url, headers=headers, data=message)

                return redirect(url_for("home"))


        elif 'button_delete' in request.form:
            selected_socode = request.form.get("button_delete")
            print ("ลบ", button_delete)
            query = "update tb_Order set states='0' WHERE SoCode = " + selected_socode
            Execute_data_insert(query)
            customer_name = request.form.get("customer")  # รับค่าชื่อจากดรอปดาวน์
            product_name = request.form.get("stock")  # รับค่าสินค้าจากดรอปดาวน์

            customer_result = Execute_data(f"select *from tbCustomer where CustCode = '{customer_name}'")
            if customer_result:
                 customer_numname = customer_result[0][2]
                 customer_na = customer_result[0][3]
                 customer_tell = customer_result[0][5]
                 customergrp_code = customer_result[0][1]

            customergrp_result = Execute_data(f"select *from tbCustomerGrp where CustGrpCode = '{customergrp_code}'")
            if customergrp_result:
                 customer_namegrp = customergrp_result[0][1]

            stock_result = Execute_data(f"select *from tbStock where StockCode = '{product_name}'")
            if stock_result:
                Stock_name = stock_result[0][4]
            
            message_text = {
                    f">> รายการการสั่งซื้อสินค้า ร้าน BakeCraft Supplies <<\n\n"
                    f"⚠️ มีการยกเลิกรายการ\n\n"
                    f"🛒 ข้อมูลการสั่งซื้อสินค้า\n"
                    f"👤 ชื่อลูกค้า: {customer_numname} {customer_na}\n"
                    f"📞 เบอร์ลูกค้า: {customer_tell}\n"
                    f"🏷️ ประเภทลูกค้า: {customer_namegrp}\n"
                    f"📦 สินค้า: {Stock_name}\n"
                }

            message = {"message": message_text}
            
            res = requests.post(url=url, headers=headers, data=message)
            return redirect(url_for("home"))
        
        
        elif 'button_fill' in request.form:
             fill_text = request.form.get("fill_text")
             print("text",fill_text)

             if fill_text.isdigit():
                    query = "select * from tb_Order where SoCode = " + fill_text
                    result_text = Execute_data(query)
                    order_text = result_text
             else :
                  query = "SELECT * FROM tbCustomer WHERE CustName = N'" + fill_text + "'"
                  result_text = Execute_data(query)
                  order_text = result_text


        return render_template("home/home.html",
                            select_value=select_value,
                            select_stock=select_stock,
                            customer_text=customer_text,
                            stock_text=stock_text,
                            stockgrp_text=stockgrp_text,
                            customergrp_text=customergrp_text,
                            order_text = order_text,
                            select_edit = select_edit

                            )

            
    else:
        print("select_value else") 

    return render_template("home/home.html",
                            select_value=select_value,
                            select_stock=select_stock,
                            customer_text=customer_text,
                            stock_text=stock_text,
                            stockgrp_text=stockgrp_text,
                            customergrp_text=customergrp_text,
                            order_text = order_text,
                            select_edit = select_edit

                            )





























@app.route("/customer")
def customer():
    result = connection_databases()

    if result > 0:

        query = "SELECT * FROM tbCustomer"
        result_customer = Execute_data(query)

        if result_customer:
                customer_text = result_customer
                print (result_customer)
        else : 
                print("")
            
        
        conn_text = "สำเร็จ"
    elif result < 0:
        conn_text = "ไม่สำเร็จ"
    return render_template("customer/customer.html",conn_text = conn_text,customer_text=customer_text) 

@app.route("/customergrp")
def customergrp():
    result = connection_databases()

    if result > 0:

        query1 = "SELECT * FROM tbCustomerGrp"
        result_customergrp = Execute_data(query1)

        if result_customergrp:
                customergrp_text = result_customergrp
                print (result_customergrp)
        else : 
                print("")
            
        
        conn_text = "สำเร็จ"
    elif result < 0:
        conn_text = "ไม่สำเร็จ"
    return render_template("customergrp/customergrp.html",conn_text = conn_text,customergrp_text=customergrp_text) 

@app.route("/stock")
def stock():
    result = connection_databases()

    if result > 0:

        query2 = "SELECT * FROM tbStock"
        result_stock = Execute_data(query2)

        if result_stock:
                stock_text = result_stock
                print (result_stock)
        else : 
                print("")
            
        
        conn_text = "สำเร็จ"
    elif result < 0:
        conn_text = "ไม่สำเร็จ"
    return render_template("stock/stock.html",conn_text = conn_text,stock_text=stock_text) 

@app.route("/stockGrp")
def stockGrp():
    result = connection_databases()

    if result > 0:

        query = "SELECT * FROM tbStockGrp"
        result_stockgrp = Execute_data(query)

        if result_stockgrp:
                stockgrp_text = result_stockgrp
                print (result_stockgrp)
        else : 
                print("")
            
        
        conn_text = "สำเร็จ"
    elif result < 0:
        conn_text = "ไม่สำเร็จ"
    return render_template("stockgrp/stockgrp.html",conn_text = conn_text,stockgrp_text=stockgrp_text) 

@app.route("/saletype")
def saletype():
    result = connection_databases()

    if result > 0:

        query = "SELECT * FROM tbSaleType"
        result_saletype = Execute_data(query)

        if result_saletype:
                saletype_text = result_saletype
                print (result_saletype)
        else : 
                print("")
            
        
        conn_text = "สำเร็จ"
    elif result < 0:
        conn_text = "ไม่สำเร็จ"
    return render_template("saletype/saletype.html",conn_text = conn_text,saletype_text= saletype_text) 

@app.route("/location")
def location():
    result = connection_databases()

    if result > 0:
            
        query = "SELECT * FROM tbLocation"
        result_location = Execute_data(query)

        if result_location:
                location_text = result_location
                print (result_location)
        else : 
                print("")
            
        
        conn_text = "สำเร็จ"
    elif result < 0:
        conn_text = "ไม่สำเร็จ"
    return render_template("location/location.html",conn_text = conn_text,location_text=location_text) 

if __name__ == "__main__":
    app.run(debug = True)
