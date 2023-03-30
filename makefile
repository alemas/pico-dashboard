.PHONY: send_src receive_src

OUT_PATH = /Volumes/PICO

send_src:
	cp -r *.py ${OUT_PATH}

receive_src:
	cp -r ${OUT_PATH}/*.py ./

# send_fonts:
# ifneq ("$(wildcard $(OUT_PATH)/fonts)", "")
# 	rm -r ${OUT_PATH}/fonts/*;
# else
# 	mkdir ${OUT_PATH}/fonts;
# endif
# 	cp -r fonts/* ${OUT_PATH}/fonts

# send_img:
# 	cp -r img ${OUT_PATH}/img

# send_lib:
# 	cp -r lib ${OUT_PATH}/lib