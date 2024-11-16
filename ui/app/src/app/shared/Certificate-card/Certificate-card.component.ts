import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Certificate-card.component.html',
  styleUrls: ['./Certificate-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Certificate-card]': 'true'
  }
})

export class CertificateCardComponent {


}