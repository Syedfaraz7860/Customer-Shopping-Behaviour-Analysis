select*from customer;

select gender, sum(purchase_amount) as revenu
from customer
group by gender;

select customer_id, purchase_amount
from customer
where discount_applied='Yes'
and purchase_amount>=(select avg(purchase_amount)from customer);

select item_purchased,
round(avg(review_rating) :: numeric,2) as "Average_rating"
from customer
group by item_purchased
order by avg(review_rating)desc
limit 5;

select shipping_type, round(avg(purchase_amount)::numeric,2)
from customer
where shipping_type in('Standard','Express')
group by shipping_type;

--subscription analysis
select subscription_status,
count(customer_id)as total_customers,
round(avg(purchase_amount),2)as avg_spend,
round(sum(purchase_amount),2) as total_revenue
from customer
group by subscription_status
order by total_revenue,avg_spend desc;

--discount dependency analysis
select item_purchased,
round(
100*sum(
case when discount_applied='Yes' then 1
else 0 end)/count(*),2) as discount_rate
from customer
group by item_purchased
order by discount_rate desc
limit 5;

--CUSTOMER SEGMENTATION---
select*from customer;

WITH customer_type AS (
    SELECT
        customer_id,
        previous_purchases,
        CASE
            WHEN previous_purchases = 1 THEN 'New'
            WHEN previous_purchases BETWEEN 2 AND 10 THEN 'Returning'
            ELSE 'Loyal'
        END AS customer_segment
    FROM customer
)

SELECT customer_segment,
count(*) as number of customers
from customer_type
group by cu

--8 product prpularity Analysis--
with item_counts as 
(
select category, item_purchased,
count(customer_id) as total_orders,
row_number() over (partition by category order by count (customer_id) desc ) as item_rank
from customer
group by category, item_purchased
) 
select item_rank, category, item_purchased, total_orders
from item_counts
where item_rank<=3;

---repeat Buyer Analysis -
select subscription_status,
count(customer_id)as repeated_buyers
from customer
where previous_purchases>5
group by subscription_status;

--Age group revenue Analysis--
sele