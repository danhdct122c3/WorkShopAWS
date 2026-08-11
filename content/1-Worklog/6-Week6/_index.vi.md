---
title: "Tuáº§n 6: TÃ­ch há»£p XÃ¡c thá»±c Äa lá»›p (Cognito)"
date: 2026-06-22
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

# Tuáº§n 6: TÃ­ch há»£p XÃ¡c thá»±c Äa lá»›p (Cognito)

**ThÃ nh viÃªn:** Backend Developer

## 1. Má»¥c tiÃªu cÃ´ng viá»‡c
Táº¡o Amazon Cognito User Pool. Viáº¿t lá»›p middleware Ä‘á»ƒ cháº·n cÃ¡c API, chá»‰ cho phÃ©p Ä‘i qua khi cÃ³ JWT Token há»£p lá»‡.

## 2. Nháº­t kÃ½ cÃ´ng viá»‡c chi tiáº¿t

| Thá»© | CÃ´ng viá»‡c | NgÃ y báº¯t Ä‘áº§u | NgÃ y hoÃ n thÃ nh | Nguá»“n tÃ i liá»‡u |
|---|---|---|---|---|
| 2 | - Thiáº¿t láº­p Amazon Cognito User Pool. Cáº¥u hÃ¬nh cÃ¡c chÃ­nh sÃ¡ch yÃªu cáº§u báº£o máº­t (Password policy). | 27/07/2026 | 27/07/2026 | TÃ i liá»‡u AWS / Github |
| 3 | - Viáº¿t script tá»± Ä‘á»™ng Ä‘á»“ng bá»™: ThÃªm User má»›i vÃ o DynamoDB sáº½ tá»± táº¡o account trong Cognito. | 28/07/2026 | 28/07/2026 | StackOverflow |
| 4 | - XÃ¢y dá»±ng lá»›p báº£o vá»‡ API (Dependency Auth). Fetch Public Keys (JWKS) tá»« Cognito vá» Ä‘á»ƒ lÆ°u cache. | 29/07/2026 | 29/07/2026 | API Docs |
| 5 | - DÃ¹ng thÆ° viá»‡n python-jose giáº£i mÃ£ vÃ  kiá»ƒm tra Signature JWT Access Token. | 30/07/2026 | 30/07/2026 | AWS Blogs |
| 6 | - Gáº¯n Dependency Auth vÃ o cÃ¡c Endpoint. Khai bÃ¡o Security Schema Ä‘á»ƒ test trá»±c tiáº¿p trÃªn Swagger UI. | 31/07/2026 | 31/07/2026 | BÃ¡o cÃ¡o tuáº§n |


## 3. CÃ¡c káº¿t quáº£ Ä‘áº¡t Ä‘Æ°á»£c
- HoÃ n thÃ nh cÃ¡c tÃ­nh nÄƒng vÃ  má»¥c tiÃªu Ä‘á» ra trong tuáº§n.
- TÃ­ch há»£p thÃ nh cÃ´ng vá»›i cÃ¡c dá»‹ch vá»¥ AWS liÃªn quan (náº¿u cÃ³).
- Äáº£m báº£o cháº¥t lÆ°á»£ng cÃ´ng viá»‡c Ä‘Ã¡p á»©ng yÃªu cáº§u cá»§a dá»± Ã¡n.

## 4. KhÃ³ khÄƒn & HÆ°á»›ng giáº£i quyáº¿t
- **KhÃ³ khÄƒn:** QuÃ¡ trÃ¬nh tÃ¬m hiá»ƒu vÃ  tÃ­ch há»£p Ä‘Ã´i lÃºc gáº·p lá»—i khÃ´ng mong muá»‘n. Cáº§n nhiá»u thá»i gian Ä‘á»c log vÃ  tÃ i liá»‡u ká»¹ thuáº­t cá»§a AWS.
- **Giáº£i phÃ¡p:** Phá»‘i há»£p cÃ¹ng cÃ¡c thÃ nh viÃªn khÃ¡c trong nhÃ³m Ä‘á»ƒ trao Ä‘á»•i, Ä‘á»c ká»¹ tÃ i liá»‡u hÆ°á»›ng dáº«n vÃ  tham kháº£o thÃªm Ã½ kiáº¿n cá»§a Mentor.

## 5. Káº¿ hoáº¡ch tuáº§n tiáº¿p theo
- RÃ  soÃ¡t láº¡i cÃ´ng viá»‡c cá»§a tuáº§n nÃ y (Review).
- Báº¯t tay vÃ o nghiÃªn cá»©u vÃ  triá»ƒn khai cÃ¡c nhiá»‡m vá»¥ cá»§a Tuáº§n 7.

