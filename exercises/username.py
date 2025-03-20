#CodelandUsernameValidation( str ) fonksiyonunun geçirilen str parametresini almasını ve dizenin geçerli bir kullanıcı adı olup olmadığını aşağıdaki kurallara göre belirlemesini sağlayın:

# 1. Kullanıcı adı 4 ila 25 karakter arasındadır.
# 2. Bir harfle başlamalıdır.
# 3. Yalnızca harf, rakam ve alt çizgi karakteri içerebilir.
# 4. Alt çizgi karakteriyle bitemez.

def CodelandUsernameValidation(strParam):
  harfler="abcçdefgĞhıijklmnoöprsştyuvzxqwQWERTYUIOPĞÜASFDGHJKLŞİZXCVBNMÖÇ"
  for i in strParam:
    if i not in harfler and type(i)!=int and i!="_":
      return False
  if strParam[0] in harfler:
    if len(strParam)>4 and len(strParam)<25:
      if strParam[-1]!="_":
        return True
      else:
        return False
    else:
      return False
  else:
    return False
print(CodelandUsernameValidation(input()))
