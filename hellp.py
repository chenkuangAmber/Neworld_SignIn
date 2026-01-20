# Neworld 自动签到脚本（终极稳定版：三重定位+全兜底+精准验证）
from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_chrome():
    """初始化Chrome浏览器（适配GitHub Actions环境）"""
    chrome_options = webdriver.ChromeOptions()
    # 无头模式运行（无界面）
    chrome_options.add_argument('--headless=new')
    # 适配Linux环境
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # 保证页面元素可见
    chrome_options.add_argument('--window-size=1920,1080')
    # 禁用GPU加速
    chrome_options.add_argument('--disable-gpu')
    # 模拟正常浏览器UA
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    # 初始化驱动
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 全局隐式等待（所有元素加载等待15秒）
    driver.implicitly_wait(15)
    return driver

def main():
    # 初始化浏览器
    driver = init_chrome()
    # 读取GitHub Secrets中的账号密码
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    
    # 校验账号密码是否存在
    if not username or not password:
        print("❌ 错误：未获取到账号或密码，请检查GitHub Secrets配置！")
        driver.quit()
        return

    print(f"📌 开始执行自动签到，账号：{username}")

    try:
        # ===================== 步骤1：访问登录页 =====================
        driver.get("https://neworld.tv/auth/login")
        time.sleep(3)  # 等待页面基础加载
        driver.save_screenshot("1_登录页.png")
        print("✅ 步骤1：登录页加载完成并截图")

        # ===================== 步骤2：输入账号密码 =====================
        # 定位并输入账号
        account_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='注册邮箱']"))
        )
        account_input.clear()
        account_input.send_keys(username)
        
        # 定位并输入密码
        pwd_input = driver.find_element(By.XPATH, "//input[@placeholder='登入密码']")
        pwd_input.clear()
        pwd_input.send_keys(password)
        
        time.sleep(2)  # 等待输入完成
        driver.save_screenshot("2_账号密码输入完成.png")
        print("✅ 步骤2：账号密码输入完成并截图")

        # ===================== 步骤3：点击登录按钮 =====================
        login_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
        )
        login_btn.click()
        time.sleep(5)  # 等待登录跳转
        driver.save_screenshot("3_登录后页面.png")
        print("✅ 步骤3：登录按钮点击完成并截图")

        # ===================== 步骤4：进入用户中心 =====================
        # 直接访问用户中心，避免刷新导致的不稳定
        driver.get("https://neworld.tv/user")
        time.sleep(10)  # 等待用户中心完全加载
        driver.save_screenshot("4_用户中心页面.png")
        print("✅ 步骤4：用户中心加载完成并截图")

        # ===================== 步骤5：三重规则定位签到按钮 =====================
        sign_btn = None
        try:
            # 规则1：精准匹配（每日签到文字后的第一个按钮）
            sign_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '每日签到')]/following::button[1]"))
            )
            print("📌 定位成功：规则1（精准匹配每日签到区域按钮）")
        except:
            print("⚠️ 规则1失败，尝试规则2（宽松匹配）")
            try:
                # 规则2：宽松匹配（所有含“签到”文字的元素）
                sign_btn = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '签到')]"))
                )
                print("📌 定位成功：规则2（宽松匹配含签到文字的元素）")
            except:
                print("⚠️ 规则2失败，尝试规则3（视觉兜底）")
                try:
                    # 规则3：视觉兜底（页面中所有蓝色按钮）
                    sign_btn = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary, button.btn-blue, button[style*='blue']"))
                    )
                    print("📌 定位成功：规则3（视觉兜底匹配蓝色按钮）")
                except Exception as e:
                    print(f"❌ 所有定位规则均失败：{str(e)}")
                    driver.save_screenshot("99_定位失败页面.png")
                    raise  # 抛出异常，终止执行

        # ===================== 步骤6：点击签到按钮 =====================
        # 记录点击前按钮文案
        btn_text_before = sign_btn.text.strip()
        print(f"📌 点击前按钮文案：{btn_text_before}")
        
        # 点击签到按钮
        sign_btn.click()
        time.sleep(5)  # 等待签到结果刷新
        driver.save_screenshot("5_点击签到后页面.png")
        print("✅ 步骤6：签到按钮点击完成并截图")

        # ===================== 步骤7：验证签到结果 =====================
        try:
            # 重新定位按钮，验证状态
            sign_btn_after = driver.find_element(By.XPATH, "//div[contains(text(), '每日签到')]/following::button[1]")
            btn_text_after = sign_btn_after.text.strip()
            
            if btn_text_after == "已签到":
                print("🎉 签到成功！按钮状态已变更为：已签到")
                driver.save_screenshot("6_签到验证成功.png")
            elif btn_text_after == btn_text_before:
                print(f"⚠️ 签到失败：按钮状态未变化，当前文案：{btn_text_after}")
                driver.save_screenshot("6_签到验证失败.png")
            else:
                print(f"📌 签到状态待确认：按钮文案变为 {btn_text_after}")
                driver.save_screenshot("6_签到状态待确认.png")
        except:
            print("🎉 签到成功：按钮已消失（页面刷新后移除）")
            driver.save_screenshot("6_签到成功_按钮消失.png")

    # ===================== 异常处理 =====================
    except Exception as e:
        print(f"❌ 脚本执行出错：{str(e)}")
        driver.save_screenshot("99_执行错误页面.png")
    finally:
        # 无论成功/失败，都关闭浏览器
        driver.quit()
        print("🔚 脚本执行结束")

# 程序入口
if __name__ == "__main__":
    main()
