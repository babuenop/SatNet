[
  {
    "model": "inventario.material",
    "pk": 1,
    "fields": {
      "codigo": "MAT001",
      "descripcion": "Cable HDMI",
      "proveedor": "Proveedor A",
      "estado": "nuevo",
      "stock": 50,
      "unidad": "und",
      "created_at": "2025-04-01T00:00:00Z",
      "updated_at": "2025-04-01T00:00:00Z"
    }
  },
  {
    "model": "inventario.actaentrega",
    "pk": 1,
    "fields": {
      "tecnico": 1,
      "fecha": "2025-04-10",
      "cerrada_por_tecnico": true
    }
  },
  {
    "model": "inventario.detalleentrega",
    "pk": 1,
    "fields": {
      "acta": 1,
      "material": 1,
      "cantidad": 10,
      "reparado_por": 1
    }
  }
]
