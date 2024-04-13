---
---

{% assign csv_data = site.data.biz.technical-writing-outline-taxonomy %}

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {% for row in csv_data %}
    <tr>
      <td>{{ row.Type }}</td>
      <td>{{ row.Description }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
