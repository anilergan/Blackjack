# Deep Q Learning Algorithm

0. Init Q value (**init model**)
1. Choose action (**model.predict(state)** or **random move**)
2. Perform action
3. Measure reward
4. Update Q value (**train model**)
5. Go to step 1

## Bellman Equation
$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R(s,a) + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

- `Q(s, a)` = Durum `s` ve aksiyon `a` için mevcut Q-değeri.
- `α` = Öğrenme oranı (learning rate).
- `r` = Ödül (reward).
- `γ` = Gelecek ödüllerin indirim faktörü (discount factor).
- `max_{a'} Q(s', a')` = Yeni durumda (`s'`) en iyi aksiyon için tahmin edilen Q-değeri.
