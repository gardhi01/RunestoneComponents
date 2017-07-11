from runestone.unittest_base import module_fixture_maker, RunestoneTestCase
from selenium.webdriver import ActionChains

setUpModule, tearDownModule = module_fixture_maker(__file__)

class ActiveCodeTests(RunestoneTestCase):
    def test_hello(self):
        '''
        1. Get the outer div id of the activecode component
        2. Find the run button using its class name
        3. Run the example
        4. Check the output from the ac_output element
        :return:
        '''
        self.driver.get(self.host + "/index.html")
        t1 = self.driver.find_element_by_id("test1")
        self.assertIsNotNone(t1)
        rb = t1.find_element_by_class_name("run-button")
        self.assertIsNotNone(rb)
        rb.click()
        output = t1.find_element_by_class_name("ac_output")
        self.assertEqual(output.text.strip(),"Hello World")


    def test_history(self):
        '''
        1. Get the outer div id of the activecode component
        2. Find the run button using its class name
        3. Run the example
        4. Check the output from the ac_output element
        :return:
        '''
        self.driver.get(self.host + "/index.html")
        t1 = self.driver.find_element_by_id("test1")
        self.assertIsNotNone(t1)
        rb = t1.find_element_by_class_name("run-button")
        self.assertIsNotNone(rb)
        rb.click()
        ta = t1.find_element_by_class_name("cm-s-default")
        self.assertIsNotNone(ta)
        self.driver.execute_script("""edList['test1'].editor.setValue("print('GoodBye')")""")
        rb.click()
        output = t1.find_element_by_class_name("ac_output")
        self.assertEqual(output.text.strip(),"GoodBye")
        move = ActionChains(self.driver)
        slider = t1.find_element_by_class_name("ui-slider")
        width = slider.size['width']
        slider = t1.find_element_by_class_name("ui-slider-handle")
        move.click_and_hold(slider).move_by_offset(-width,0).release().perform()
        rb.click()
        output = t1.find_element_by_class_name("ac_output")
        self.assertEqual(output.text.strip(), "Hello World")
