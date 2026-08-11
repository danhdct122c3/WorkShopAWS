---
title: "Tuáº§n 5: Xá»­ lÃ½ Upload file (Presigned URL)"
date: 2026-06-22
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

# Tuáº§n 5: Xá»­ lÃ½ Upload file (Presigned URL)

**ThÃ nh viÃªn:** Backend Developer

## 1. Má»¥c tiÃªu cÃ´ng viá»‡c
Xá»­ lÃ½ bÃ i toÃ¡n upload báº±ng cÃ¡ch cáº¥p phÃ¡t Presigned URL (AWS S3) thay vÃ¬ táº£i qua API Gateway Ä‘á»ƒ trÃ¡nh timeout vÃ  limit dung lÆ°á»£ng.

## 2. Nháº­t kÃ½ cÃ´ng viá»‡c chi tiáº¿t

| Thá»© | CÃ´ng viá»‡c | NgÃ y báº¯t Ä‘áº§u | NgÃ y hoÃ n thÃ nh | Nguá»“n tÃ i liá»‡u |
|---|---|---|---|---|
| 2 | - PhÃ¢n tÃ­ch háº¡n cháº¿ táº£i file qua API Gateway (10MB limit). LÃªn phÆ°Æ¡ng Ã¡n dÃ¹ng S3 Presigned URL. | 20/07/2026 | 20/07/2026 | TÃ i liá»‡u AWS / Github |
| 3 | - Thiáº¿t láº­p bucket S3 lÆ°u trá»¯ bÃ¡o cÃ¡o. Cáº¥u hÃ¬nh CORS policy Ä‘á»ƒ Frontend cÃ³ thá»ƒ upload chÃ©o domain. | 21/07/2026 | 21/07/2026 | StackOverflow |
| 4 | - Viáº¿t API `/tasks/presigned-url` gá»i hÃ m `generate_presigned_url` cá»§a boto3 sinh link táº¡m thá»i. | 22/07/2026 | 22/07/2026 | API Docs |
| 5 | - TÃ­ch há»£p API lÆ°u thÃ´ng tin metadata cá»§a file (URL, tÃªn file) vÃ o báº£ng Tasks trÃªn DynamoDB. | 23/07/2026 | 23/07/2026 | AWS Blogs |
| 6 | - Thiáº¿t láº­p Validation Content-Type cháº·n upload cÃ¡c file mÃ£ Ä‘á»™c, há»— trá»£ team debug luá»“ng upload. | 24/07/2026 | 24/07/2026 | BÃ¡o cÃ¡o tuáº§n |


## 3. CÃ¡c káº¿t quáº£ Ä‘áº¡t Ä‘Æ°á»£c
- HoÃ n thÃ nh cÃ¡c tÃ­nh nÄƒng vÃ  má»¥c tiÃªu Ä‘á» ra trong tuáº§n.
- TÃ­ch há»£p thÃ nh cÃ´ng vá»›i cÃ¡c dá»‹ch vá»¥ AWS liÃªn quan (náº¿u cÃ³).
- Äáº£m báº£o cháº¥t lÆ°á»£ng cÃ´ng viá»‡c Ä‘Ã¡p á»©ng yÃªu cáº§u cá»§a dá»± Ã¡n.

## 4. KhÃ³ khÄƒn & HÆ°á»›ng giáº£i quyáº¿t
- **KhÃ³ khÄƒn:** QuÃ¡ trÃ¬nh tÃ¬m hiá»ƒu vÃ  tÃ­ch há»£p Ä‘Ã´i lÃºc gáº·p lá»—i khÃ´ng mong muá»‘n. Cáº§n nhiá»u thá»i gian Ä‘á»c log vÃ  tÃ i liá»‡u ká»¹ thuáº­t cá»§a AWS.
- **Giáº£i phÃ¡p:** Phá»‘i há»£p cÃ¹ng cÃ¡c thÃ nh viÃªn khÃ¡c trong nhÃ³m Ä‘á»ƒ trao Ä‘á»•i, Ä‘á»c ká»¹ tÃ i liá»‡u hÆ°á»›ng dáº«n vÃ  tham kháº£o thÃªm Ã½ kiáº¿n cá»§a Mentor.

## 5. Káº¿ hoáº¡ch tuáº§n tiáº¿p theo
- RÃ  soÃ¡t láº¡i cÃ´ng viá»‡c cá»§a tuáº§n nÃ y (Review).
- Báº¯t tay vÃ o nghiÃªn cá»©u vÃ  triá»ƒn khai cÃ¡c nhiá»‡m vá»¥ cá»§a Tuáº§n 6.

