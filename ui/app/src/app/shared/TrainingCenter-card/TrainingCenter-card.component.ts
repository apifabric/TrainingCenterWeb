import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './TrainingCenter-card.component.html',
  styleUrls: ['./TrainingCenter-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.TrainingCenter-card]': 'true'
  }
})

export class TrainingCenterCardComponent {


}